from fastapi.testclient import TestClient

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
