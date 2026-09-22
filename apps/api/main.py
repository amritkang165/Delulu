from __future__ import annotations

import re
import os
from typing import Literal

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field


class IdeaRequest(BaseModel):
    startupName: str = Field(min_length=1, max_length=120)
    ideaDescription: str = Field(min_length=1, max_length=2000)
    targetCustomer: str = Field(min_length=1, max_length=500)
    problem: str = Field(min_length=1, max_length=2000)
    solution: str = Field(min_length=1, max_length=2000)
    industry: str = Field(min_length=1, max_length=80)
    businessModel: str = Field(min_length=1, max_length=120)


class Scores(BaseModel):
    problemClarity: int = Field(ge=1, le=10)
    customerUrgency: int = Field(ge=1, le=10)
    technicalComplexity: int = Field(ge=1, le=10)
    monetizationClarity: int = Field(ge=1, le=10)
    acquisitionDifficulty: int = Field(ge=1, le=10)
    competitionLevel: int = Field(ge=1, le=10)


class EvaluationResponse(BaseModel):
    scores: Scores
    uncertainty: int = Field(ge=1, le=10)
    risks: list[str]
    recommendation: str
    roast: str
    source: Literal["illustrative-rule-engine"] = "illustrative-rule-engine"


class MarketReportRequest(BaseModel):
    ideaDescription: str = Field(min_length=1, max_length=4000)
    targetCustomer: str = Field(default="", max_length=1000)
    industry: str = Field(default="", max_length=120)


class MarketCompany(BaseModel):
    name: str
    status: Literal["active", "failed", "unknown"]
    description: str
    revenue: str | None = None
    revenueSource: str | None = None
    source: str


class MarketReportResponse(BaseModel):
    status: Literal["provider_required", "complete"]
    query: str
    similarCount: int | None = None
    executedCount: int | None = None
    competitors: list[MarketCompany] = []
    failedPlayers: list[MarketCompany] = []
    caveats: list[str]
    sources: list[str] = []


app = FastAPI(title="DeluluScore API", version="0.1.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def score_text(text: str, fallback: int = 4) -> int:
    words = len(text.strip().split())
    return min(9, max(2, fallback + round(words / 18)))


def evaluate_idea(idea: IdeaRequest) -> EvaluationResponse:
    combined = " ".join(idea.model_dump().values()).lower()
    has_evidence = bool(re.search(r"user|customer|interview|pilot|paying|revenue|waitlist|prototype|validated", combined))
    complexity_boost = 2 if re.search(r"marketplace|hardware|blockchain|delivery|network|platform|real-time|integration", combined) else 0
    competition_boost = 2 if re.search(r"ai|invoice|tutor|resume|delivery|productivity|analytics|marketplace", combined) else 0
    scores = Scores(
        problemClarity=score_text(idea.problem, 4),
        customerUrgency=score_text(f"{idea.problem} {idea.targetCustomer}", 3),
        technicalComplexity=min(10, 3 + complexity_boost + round(len(idea.solution) / 140)),
        monetizationClarity=3 if idea.businessModel == "No clear model yet" else 6 if idea.businessModel == "Subscription" else 5,
        acquisitionDifficulty=min(10, 4 + round(len(idea.targetCustomer) / 40)),
        competitionLevel=min(10, 3 + competition_boost),
    )
    uncertainty = round(sum(scores.model_dump().values()) / len(scores.model_dump()) + (-1 if has_evidence else 1))
    risks = []
    if not has_evidence:
        risks.append("No customer evidence is visible yet. The idea is still carrying its assumptions in a backpack.")
    if scores.technicalComplexity >= 6:
        risks.append("The first version may be overbuilt before the core demand is proven.")
    if scores.acquisitionDifficulty >= 6:
        risks.append("Distribution looks harder than the product pitch makes it sound.")
    if scores.competitionLevel >= 6:
        risks.append("Existing alternatives will make differentiation and retention do real work.")
    return EvaluationResponse(
        scores=scores,
        uncertainty=min(10, max(1, uncertainty)),
        risks=risks,
        recommendation=(
            "Run a narrow paid pilot with the exact customer segment you named. Measure repeat use before adding features."
            if has_evidence
            else "Interview five people in the target segment this week. Ask about the last time this problem cost them time, money, or patience."
        ),
        roast=(
            "The architecture is already wearing a tiny graduation cap. Make sure it has met a customer before it starts giving a thesis defense."
            if scores.technicalComplexity >= 7
            else f"You have a {uncertainty}/10 uncertainty problem, which is healthier than a 10/10 confidence problem. Go find the receipts."
        ),
    )


@app.get("/api/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "deluluscore-api"}


@app.post("/api/evaluate", response_model=EvaluationResponse)
def evaluate(idea: IdeaRequest) -> EvaluationResponse:
    return evaluate_idea(idea)


@app.post("/api/market-report", response_model=MarketReportResponse)
def market_report(request: MarketReportRequest) -> MarketReportResponse:
    provider_url = os.getenv("MARKET_RESEARCH_API_URL")
    if not provider_url:
        return MarketReportResponse(
            status="provider_required",
            query=request.ideaDescription,
            caveats=[
                "No market-research provider is configured yet.",
                "Competitor counts, execution status, revenue, and failure analysis require cited external sources.",
                "The app will not invent companies or financial figures from an idea description.",
            ],
        )
    raise NotImplementedError(
        "Configure the provider adapter for MARKET_RESEARCH_API_URL before enabling live research."
    )
