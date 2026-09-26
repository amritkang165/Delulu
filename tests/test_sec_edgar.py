import json

from apps.api import sec_edgar


def test_sec_requests_send_configured_user_agent(monkeypatch) -> None:
    user_agent = "DeluluScore contact: test@example.com"
    request_urls = []
    responses = [
        {"0": {"cik_str": 123, "ticker": "EXM", "title": "Example Inc"}},
        {
            "name": "Example Inc",
            "filings": {"recent": {"form": ["10-K"], "filingDate": ["2026-02-01"]}},
        },
    ]

    class FakeResponse:
        def __init__(self, payload):
            self.payload = payload

        def __enter__(self):
            return self

        def __exit__(self, *args):
            return None

        def read(self):
            return json.dumps(self.payload).encode()

    def fake_urlopen(request, timeout):
        assert request.get_header("User-agent") == user_agent
        assert timeout == 15
        request_urls.append(request.full_url)
        return FakeResponse(responses.pop(0))

    monkeypatch.setattr(sec_edgar, "urlopen", fake_urlopen)

    record = sec_edgar.lookup_company("Example Inc", user_agent)

    assert record["registrationId"] == "CIK 0000000123"
    assert record["status"] == "Latest SEC filing: 10-K on 2026-02-01"
    assert request_urls == [
        "https://www.sec.gov/files/company_tickers.json",
        "https://data.sec.gov/submissions/CIK0000000123.json",
    ]