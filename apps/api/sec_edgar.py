from __future__ import annotations

import json
import re
from typing import Any
from urllib.request import Request, urlopen


COMPANY_TICKERS_URL = "https://www.sec.gov/files/company_tickers.json"
SUBMISSIONS_URL = "https://data.sec.gov/submissions/CIK{cik}.json"


def _get_json(url: str, user_agent: str) -> Any:
    request = Request(url, headers={"User-Agent": user_agent, "Accept-Encoding": "gzip, deflate"})
    with urlopen(request, timeout=15) as response:
        return json.load(response)


def _normalize_company_name(name: str) -> str:
    return re.sub(r"[^a-z0-9]", "", name.casefold())


def lookup_company(company_name: str, user_agent: str) -> dict[str, str] | None:
    """Look up an exact SEC filer-name match and return its latest filing metadata."""
    tickers = _get_json(COMPANY_TICKERS_URL, user_agent)
    normalized_name = _normalize_company_name(company_name)
    match = next(
        (
            item
            for item in tickers.values()
            if _normalize_company_name(item.get("title", "")) == normalized_name
        ),
        None,
    )
    if match is None:
        return None

    cik = str(match["cik_str"]).zfill(10)
    submissions_url = SUBMISSIONS_URL.format(cik=cik)
    submissions = _get_json(submissions_url, user_agent)
    recent_filings = submissions.get("filings", {}).get("recent", {})
    forms = recent_filings.get("form", [])
    filed_dates = recent_filings.get("filingDate", [])
    filing_status = (
        f"Latest SEC filing: {forms[0]} on {filed_dates[0]}"
        if forms and filed_dates
        else "SEC filer; no recent filing listed"
    )
    return {
        "authority": "sec",
        "legalName": submissions.get("name") or match["title"],
        "registrationId": f"CIK {cik}",
        "status": filing_status,
        "sourceUrl": submissions_url,
    }