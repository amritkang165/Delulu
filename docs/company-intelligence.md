# Company Intelligence

The company report workflow accepts a startup name and is designed to combine:

- Crunchbase, Dealroom, and Tracxn for company, funding, and market records.
- Companies House and SEC EDGAR for official registration and filing verification.
- A news provider for recent reporting and event context.
- An AI provider for a cited narrative report.

## Evidence rules

Every company fact must retain its provider and source URL. Revenue must be reported as disclosed, estimated, or unavailable; estimates must never be presented as filings. A failed-company claim must identify the event source and distinguish shutdown, acquisition, dormancy, or restructuring.

## Configuration

Copy `.env.example` to `.env` and provide the credentials available to your deployment. The API currently reports provider readiness and does not fabricate results when a provider is absent. Provider adapters should normalize into the response models in `apps/api/company_intelligence.py` before the AI stage is enabled.
