from fastapi.testclient import TestClient

from apps.api import company_intelligence
from apps.api.main import app


client = TestClient(app)


VALID_IDEA = {
    "startupName": "LaundryLoop",
    "ideaDescription": "A marketplace connecting students with nearby laundry services.",
    "targetCustomer": "College students living in hostels",
    "problem": "Students need reliable and affordable laundry services.",
    "solution": "A simple booking app with local pickup scheduling.",
    "industry": "Marketplace",
    "businessModel": "Subscription",
}


def test_health_check() -> None:
    response = client.get("/api/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok", "service": "deluluscore-api"}


def test_evaluate_returns_report_contract() -> None:
    response = client.post("/api/evaluate", json=VALID_IDEA)
    body = response.json()

    assert response.status_code == 200
    assert 1 <= body["uncertainty"] <= 10
    assert set(body["scores"]) == {
        "problemClarity",
        "customerUrgency",
        "technicalComplexity",
        "monetizationClarity",
        "acquisitionDifficulty",
        "competitionLevel",
    }
    assert body["source"] == "illustrative-rule-engine"
    assert body["risks"]
    assert body["recommendation"]
    assert body["roast"]


def test_evaluate_rejects_empty_required_fields() -> None:
    invalid_idea = {**VALID_IDEA, "startupName": ""}

    response = client.post("/api/evaluate", json=invalid_idea)

    assert response.status_code == 422


def test_market_report_is_explicit_when_provider_is_missing() -> None:
    response = client.post(
        "/api/market-report",
        json={
            "ideaDescription": "A marketplace for local laundry services",
            "targetCustomer": "College students",
            "industry": "Marketplace",
        },
    )

    assert response.status_code == 200
    assert response.json()["status"] == "provider_required"
    assert response.json()["similarCount"] is None
    assert response.json()["competitors"] == []


def test_company_report_includes_sec_record_and_citations(monkeypatch) -> None:
    monkeypatch.setenv("SEC_USER_AGENT", "DeluluScore contact: test@example.com")
    captured = {}

    def fake_lookup(name, user_agent):
        captured["user_agent"] = user_agent
        return {
            "authority": "sec",
            "legalName": name,
            "registrationId": "CIK 0000000123",
            "status": "Latest SEC filing: 10-K on 2026-02-01",
            "sourceUrl": "https://data.sec.gov/submissions/CIK0000000123.json",
        }

    monkeypatch.setattr(
        company_intelligence,
        "lookup_company",
        fake_lookup,
    )

    response = client.post("/api/company-report", json={"startupName": "Example Inc"})
    body = response.json()

    assert response.status_code == 200
    assert body["status"] == "complete"
    assert captured["user_agent"] == "DeluluScore contact: test@example.com"
    assert body["officialRecords"][0]["registrationId"] == "CIK 0000000123"
    sec_status = next(item for item in body["sourceStatuses"] if item["provider"] == "sec")
    assert sec_status["status"] == "available"
    assert "https://data.sec.gov/submissions/CIK0000000123.json" in sec_status["citations"]
