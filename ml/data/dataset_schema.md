# DeluluScore Dataset Schema

Each row represents one startup idea evaluated using the DeluluScore rubric.

## Identification Fields

| Field | Type | Description |
|---|---|---|
| idea_id | string | Unique identifier |
| startup_name | string | Name of the startup |
| idea_description | text | Description of the startup idea |
| target_customer | text | Intended customer segment |
| problem_statement | text | Problem being solved |
| proposed_solution | text | Proposed solution |
| industry | categorical | Industry or domain |
| business_model | categorical | How the startup intends to make money |

## Evaluation Features

All scores range from 1 to 10.

| Field | Type | Description |
|---|---|---|
| problem_clarity | integer | How clearly the problem is defined |
| customer_urgency | integer | How urgently customers need a solution |
| technical_complexity | integer | Difficulty of building the proposed solution |
| monetization_clarity | integer | Clarity of the revenue model |
| acquisition_difficulty | integer | Difficulty of acquiring customers |
| competition_level | integer | Intensity of existing competition |
| validation_evidence | integer | Evidence that customers actually want this |
| mvp_complexity | integer | Difficulty of building a minimal viable product |

## Target Variables

| Field | Type | Description |
|---|---|---|
| overall_uncertainty | integer | Overall business and execution uncertainty |
| validation_readiness | categorical | Needs Discovery, Needs Validation, or MVP Ready |
| startup_archetype | categorical | SaaS, Marketplace, Consumer App, etc. |

## Metadata

| Field | Type | Description |
|---|---|---|
| annotation_explanation | text | Reasoning behind the assigned scores |
| annotator_id | string | Anonymous evaluator identifier |
| rubric_version | string | Version of the scoring rubric |
| data_source | categorical | Human, public, synthetic, or user-submitted |