from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path
from typing import Literal

from dotenv import load_dotenv
from pydantic import BaseModel, Field

from .sec_edgar import COMPANY_TICKERS_URL, lookup_company


load_dotenv(Path(__file__).resolve().parents[2] / ".env")

ProviderName = Literal[
    "crunchbase",
    "dealroom",
    "tracxn",
    "companies_house",
    "sec",
    "news",
    "ai_report",
]


class SourceStatus(BaseModel):
    provider: ProviderName
    status: Literal["available", "not_configured", "not_implemented", "error"]
    message: str
    citations: list[str] = Field(default_factory=list)


class CompanyRecord(BaseModel):
    name: str
    provider: Literal["crunchbase", "dealroom", "tracxn"]
    description: str | None = None
    status: Literal["active", "failed", "unknown"] = "unknown"
    foundedYear: int | None = None
    headquarters: str | None = None
    funding: str | None = None
    revenue: str | None = None
    sourceUrl: str | None = None


class OfficialRecord(BaseModel):
    authority: Literal["companies_house", "sec"]
    legalName: str | None = None
    registrationId: str | None = None
    status: str | None = None
    incorporationDate: str | None = None
    sourceUrl: str | None = None


class NewsItem(BaseModel):
    title: str
    publishedAt: str | None = None
    summary: str | None = None
    sourceUrl: str
    sourceName: str | None = None


class CompanyReportRequest(BaseModel):
    startupName: str = Field(min_length=1, max_length=160)
    website: str | None = Field(default=None, max_length=500)
    jurisdiction: str | None = Field(default=None, max_length=80)


class CompanyReportResponse(BaseModel):
    status: Literal["provider_required", "complete"]
    startupName: str
    summary: str
    companies: list[CompanyRecord] = Field(default_factory=list)
    officialRecords: list[OfficialRecord] = Field(default_factory=list)
    news: list[NewsItem] = Field(default_factory=list)
    sourceStatuses: list[SourceStatus]
    aiReport: str | None = None
    aiReportStatus: Literal["provider_required", "not_generated", "generated"] = "not_generated"
    limitations: list[str] = Field(default_factory=list)


@dataclass(frozen=True)
class ProviderConfig:
    name: ProviderName
    env_var: str
    label: str


PROVIDERS = (
    ProviderConfig("crunchbase", "CRUNCHBASE_API_KEY", "Crunchbase"),
    ProviderConfig("dealroom", "DEALROOM_API_KEY", "Dealroom"),
    ProviderConfig("tracxn", "TRACXN_API_KEY", "Tracxn"),
    ProviderConfig("companies_house", "COMPANIES_HOUSE_API_KEY", "Companies House"),
    ProviderConfig("sec", "SEC_USER_AGENT", "SEC EDGAR"),
    ProviderConfig("news", "NEWS_API_KEY", "News API"),
    ProviderConfig("ai_report", "LLM_API_KEY", "AI report provider"),
)


def source_statuses() -> list[SourceStatus]:
    statuses = []
    for provider in PROVIDERS:
        if os.getenv(provider.env_var):
            if provider.name == "sec":
                message = "SEC_USER_AGENT is configured; the SEC EDGAR adapter is connected."
                status = "available"
                statuses.append(
                    SourceStatus(provider=provider.name, status=status, message=message)
                )
                continue
            message = f"{provider.label} credentials are configured; provider adapter is the next integration step."
            status = "not_implemented"
        else:
            message = f"Set {provider.env_var} to enable {provider.label} research."
            status = "not_configured"
        statuses.append(SourceStatus(provider=provider.name, status=status, message=message))
    return statuses


def build_company_report(request: CompanyReportRequest) -> CompanyReportResponse:
    statuses = source_statuses()
    sec_agent = os.getenv("SEC_USER_AGENT", "").strip()
    official_records: list[OfficialRecord] = []
    sec_status = next(status for status in statuses if status.provider == "sec")
    limitations = [
        "Revenue figures must come from cited filings or a provider disclosure, not estimates presented as facts.",
        "Failure analysis needs a source-backed event and should distinguish shutdown, acquisition, and dormancy.",
        "AI summaries must receive retrieved evidence and citations as input; they must not invent company facts.",
    ]

    if sec_agent:
        try:
            record_data = lookup_company(request.startupName, sec_agent)
            sec_status.status = "available"
            sec_status.message = "SEC EDGAR lookup completed using the configured contact identifier."
            sec_status.citations = [COMPANY_TICKERS_URL]
            if record_data:
                official_records.append(OfficialRecord(**record_data))
                sec_status.citations.append(record_data["sourceUrl"])
            else:
                limitations.append(
                    "No exact company-name match was found in the SEC filer index. The company may be private, non-US, or listed under another legal name."
                )
        except (OSError, TimeoutError, ValueError, KeyError, TypeError):
            sec_status.status = "error"
            sec_status.message = "SEC EDGAR could not be reached or returned an unreadable response."
            limitations.append("SEC EDGAR lookup failed; no official SEC record is being claimed.")

    sec_available = sec_status.status == "available"
    if official_records:
        summary = "SEC EDGAR returned an official filing record. Other company-data providers are not connected yet."
    elif sec_available:
        summary = "SEC EDGAR was checked, but no exact-name filer match was found. Other company-data providers are not connected yet."
    elif sec_status.status == "error":
        summary = "SEC EDGAR lookup failed; no verified company record is available."
    else:
        summary = "No company-intelligence providers are configured yet."

    return CompanyReportResponse(
        status="complete" if sec_available else "provider_required",
        startupName=request.startupName,
        summary=summary,
        officialRecords=official_records,
        sourceStatuses=statuses,
        limitations=limitations,
    )
