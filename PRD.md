# 🦄 DeluluScore

## Product Requirements Document

**Version:** 0.1.0
**Status:** Draft
**Product Type:** Comedy-first startup idea analysis platform
**Tagline:** Every startup idea deserves a reality check.

---

## 1. Product Overview

DeluluScore is a comedy-first startup idea analysis engine that combines structured evaluation, classical machine learning, and AI-generated roasts to help founders identify weak assumptions before investing significant time and resources.

Users submit a startup idea and receive:

* A structured uncertainty assessment.
* Dimension-wise scores.
* Detected risks and questionable assumptions.
* Actionable recommendations.
* A personalized AI-generated roast.
* An optional shareable report.

The product uses humor to make serious startup analysis engaging.

---

## 2. Problem Statement

Early-stage founders frequently evaluate startup ideas based on excitement, trends, intuition, and confirmation bias.

Common problems include:

* Building before validating the problem.
* Overengineering the MVP.
* Adding unnecessary technologies.
* Underestimating customer acquisition.
* Having unclear monetization.
* Ignoring existing alternatives.
* Confusing technical novelty with customer value.

Existing startup evaluation tools are often generic, overly serious, or dependent on opaque AI-generated opinions.

DeluluScore aims to make startup evaluation approachable, entertaining, and structured while exposing the assumptions behind its conclusions.

---

## 3. Vision

Build the most entertaining and intellectually honest startup reality-check tool on the internet.

The product should make users laugh first, think second, and improve their idea third.

---

## 4. Goals

### Primary Goals

1. Allow users to submit and evaluate startup ideas.
2. Produce structured assessments across meaningful dimensions.
3. Train and evaluate real ML models using labeled data.
4. Generate personalized, evidence-grounded startup roasts.
5. Provide actionable recommendations.
6. Make results easy to understand and share.
7. Create a distinctive open-source portfolio project.

### Secondary Goals

* Collect anonymized feedback for model improvement.
* Allow users to compare different versions of an idea.
* Demonstrate practical classical ML engineering.
* Build a foundation for future startup intelligence features.

---

## 5. Non-Goals

DeluluScore will not:

* Predict startup success with certainty.
* Guarantee investment outcomes.
* Replace professional market research.
* Act as a financial, legal, or regulatory advisor.
* Claim that a high Delulu Score means an idea is objectively bad.
* Use arbitrary LLM-generated numbers as ground truth.
* Present subjective estimates as verified facts.

The product evaluates uncertainty and assumption risk based on available information.

---

## 6. Target Audience

### Primary Users

* College students with startup ideas.
* Hackathon participants.
* First-time founders.
* Indie hackers.
* Early-stage builders.
* Startup enthusiasts.

### Secondary Users

* Entrepreneurship clubs.
* Startup communities.
* Incubators and accelerators.
* Product managers.
* Startup mentors.

---

## 7. Product Personality

### Brand Characteristics

* Funny.
* Direct.
* Playful.
* Insightful.
* Slightly ruthless.
* Constructive.
* Self-aware.

### Communication Style

Roast business assumptions, strategies, and unnecessary complexity.

Do not attack users personally.

### Example

> You have designed a 14-service microservice architecture for a product with zero users. The infrastructure is ready. The customers remain theoretical.

---

# 8. Core User Journey

1. User visits the landing page.
2. User enters a startup idea.
3. User completes a structured questionnaire.
4. Backend validates and processes the input.
5. Feature extraction generates model-ready features.
6. ML models produce structured predictions.
7. Recommendation engine identifies risks.
8. LLM generates a roast grounded in actual findings.
9. User receives a Delulu Report.
10. User can provide feedback or modify assumptions.

---

# 9. MVP Scope

## Included

* Landing page.
* Startup idea submission.
* Structured questionnaire.
* Initial labeled dataset.
* Data preprocessing pipeline.
* Baseline regression model.
* Baseline classification model.
* Cross-validation and evaluation reports.
* FastAPI inference endpoint.
* AI-generated roast.
* Results dashboard.
* Feedback collection.
* Model version tracking.

## Excluded from MVP

* Payments.
* Public leaderboard.
* Social feed.
* Full market research automation.
* Live competitor scraping.
* Mobile application.
* Automated investment recommendations.
* Complex agent workflows.
* Advanced user account system.

---

# 10. User Inputs

## Required Inputs

* Startup name.
* Startup idea description.
* Target customer.
* Problem being solved.
* Proposed solution.
* Industry/category.
* Business model.

## Optional Inputs

* Existing competitors.
* Customer interviews completed.
* Paying users.
* Prototype status.
* Founder/team size.
* Available budget.
* Available development time.
* Technical dependencies.
* Regulatory dependencies.
* Existing traction.

## Structured Evaluation Inputs

Each relevant dimension is rated using a defined rubric, initially on a 1–10 scale:

* Problem clarity.
* Customer urgency.
* Technical complexity.
* Monetization clarity.
* Customer acquisition difficulty.
* Competitive intensity.
* Validation evidence.
* MVP scope complexity.

Each value must be identified as one of:

* User-provided.
* Human-annotated.
* Extracted from text.
* Model-predicted.
* Rule-derived.

---

# 11. Evaluation Dimensions

## 11.1 Problem Reality

Measures how clearly the idea identifies a meaningful problem and whether the problem appears frequent or painful.

## 11.2 Technical Feasibility

Measures the difficulty of building a credible MVP given the proposed technology, integrations, infrastructure, and constraints.

## 11.3 Customer Acquisition Difficulty

Measures how difficult it may be to reach and acquire the intended users.

## 11.4 Monetization Uncertainty

Measures how clearly the idea explains who pays, what they pay for, and why they would pay.

## 11.5 Competitive Pressure

Measures the presence of alternatives and the difficulty of differentiation.

## 11.6 Validation Readiness

Measures how much evidence exists that the problem and proposed solution deserve further investment.

## 11.7 MVP Complexity

Measures the scope and number of dependencies required to launch a useful first version.

---

# 12. Score Semantics

The primary score represents startup uncertainty and assumption risk.

It does not represent the probability of failure.

### Higher score means:

* More assumptions remain unvalidated.
* More execution risks are present.
* More uncertainty exists in the available information.

### Lower score means:

* The idea is more clearly defined.
* More assumptions have supporting evidence.
* The proposed MVP appears more constrained or understandable.

Dimension-level explanations must accompany any composite score.

---

# 13. Machine Learning Requirements

## 13.1 Model Objectives

### Regression

Predict human-rated scores such as:

* MVP feasibility.
* Overall uncertainty.
* Validation readiness.

### Classification

Predict categories such as:

* Needs discovery.
* Needs validation.
* MVP-ready.

### Multi-class Classification

Classify startup archetypes such as:

* SaaS.
* Marketplace.
* Developer tool.
* Consumer application.
* DeepTech.
* Hardware.
* AI application.
* Blockchain/Web3.
* D2C.

---

## 13.2 Candidate Models

### Baselines

* Mean/median predictor.
* Dummy classifier.

### Classical ML Models

* Ridge Regression.
* Logistic Regression.
* Random Forest.
* Gradient Boosting.

The simplest credible baseline must be established before using more complex models.

---

## 13.3 Preprocessing

* Missing value handling.
* Numerical scaling where appropriate.
* Categorical encoding.
* Text feature extraction.
* Feature selection.
* Leakage prevention.
* Reproducible Scikit-learn Pipelines.

---

## 13.4 Evaluation Metrics

### Regression

* MAE.
* RMSE.
* R².

### Classification

* Accuracy.
* Precision.
* Recall.
* F1-score.
* Confusion matrix.
* Balanced accuracy where class imbalance exists.

The project must report performance on held-out data and document dataset limitations.

---

# 14. Data Strategy

## Data Sources

1. Human-labeled startup ideas.
2. Publicly available startup descriptions where usage is permitted.
3. Synthetic ideas for pipeline testing.
4. Optional user feedback and evaluations.

Synthetic data must not be presented as real-world ground truth.

## Initial Dataset Target

* 100–200 startup ideas for the first research iteration.
* Multiple human evaluations per idea where possible.
* Versioned annotation rubric.
* Documented label definitions.
* Inter-rater agreement analysis.

This dataset is for experimentation, not proof of generalized startup prediction capability.

---

## Annotation Process

Each annotation should store:

* Idea ID.
* Annotator ID or anonymized identifier.
* Rubric version.
* Dimension scores.
* Confidence.
* Optional explanation.
* Timestamp.

Annotators should evaluate ideas using the same rubric.

---

# 15. Roast Engine

## Purpose

Convert structured findings into funny, specific, and useful commentary.

## Inputs

* Model predictions.
* Detected risk patterns.
* User-provided startup description.
* Recommendations.
* Selected roast intensity.

## Roast Modes

### Soft

Friendly and encouraging.

### Honest

Direct and practical.

### Brutal

Ruthless toward questionable assumptions.

## Rules

The roast engine must:

* Use supplied findings as evidence.
* Avoid fabricating statistics.
* Avoid claiming certainty.
* Avoid personal harassment.
* Roast business assumptions and decisions.
* Include at least one constructive recommendation.
* Clearly separate humor from factual analysis.

### Example

Finding:

* High technical complexity.
* Low validation evidence.
* Unclear monetization.

Roast:

> Your MVP requires blockchain, AI, and a two-sided marketplace before serving its first customer. That's not an MVP. That's a cry for venture capital.

---

# 16. Recommendation Engine

The recommendation engine maps detected patterns to actionable suggestions.

| Detected Pattern          | Recommendation                           |
| ------------------------- | ---------------------------------------- |
| High technical complexity | Reduce MVP scope                         |
| Low validation evidence   | Conduct customer interviews              |
| Unclear monetization      | Test willingness to pay                  |
| High competition          | Identify specific differentiation        |
| Too many integrations     | Remove nonessential dependencies         |
| Broad target audience     | Narrow the initial customer segment      |
| AI without clear need     | Validate whether automation is necessary |

Recommendations must be traceable to specific findings.

---

# 17. Functional Requirements

## FR-01: Idea Submission

Users must be able to submit a startup idea and relevant context.

## FR-02: Input Validation

The backend must validate required fields, field lengths, and accepted values.

## FR-03: Feature Extraction

The system must transform structured and textual inputs into model-ready features.

## FR-04: Model Inference

The backend must return predictions using a versioned model.

## FR-05: Report Generation

The system must generate a report containing:

* Overall uncertainty score.
* Dimension scores.
* Confidence indicators.
* Detected risks.
* Recommendations.
* AI-generated roast.

## FR-06: Feedback

Users should be able to rate whether the report was useful and whether the assessment seemed reasonable.

## FR-07: Reproducibility

The same model version and input should produce reproducible structured predictions, subject to documented stochastic components.

## FR-08: Model Metadata

Every prediction must store the model version and relevant rubric version.

---

# 18. Non-Functional Requirements

## Performance

* Analysis requests should return within a reasonable interactive timeframe.
* LLM generation should not unnecessarily block ML inference.

## Reliability

* Invalid input must return clear errors.
* LLM failures must not prevent structured ML results from being displayed.

## Security

* API keys must remain server-side.
* User-submitted content must be treated as untrusted input.
* No sensitive personal data should be required.
* Logs must avoid storing secrets.

## Privacy

* Users should be informed about data storage.
* Public sharing must be opt-in.
* Training use of user submissions must require appropriate consent.

## Accessibility

* Results must not rely exclusively on color.
* Charts must have text alternatives.
* Keyboard navigation should be supported.

---

# 19. System Architecture

## Frontend

Next.js application responsible for:

* Landing page.
* Submission flow.
* Loading state.
* Results dashboard.
* Feedback interface.
* Report sharing.

## Backend

FastAPI responsible for:

* Request validation.
* Feature extraction orchestration.
* Model inference.
* Recommendation generation.
* Roast generation.
* Persistence.
* Model metadata.

## ML Package

Independent Python package containing:

* Dataset loading.
* Preprocessing.
* Feature engineering.
* Training.
* Evaluation.
* Inference.
* Model serialization.

## Database

PostgreSQL stores:

* Startup ideas.
* Structured features.
* Human evaluations.
* Model predictions.
* Feedback.
* Model metadata.

---

# 20. Suggested API Endpoints

| Method | Endpoint                         | Purpose                 |
| ------ | -------------------------------- | ----------------------- |
| POST   | `/api/v1/ideas`                  | Create a startup idea   |
| POST   | `/api/v1/analyze`                | Analyze a startup idea  |
| GET    | `/api/v1/analyses/{analysis_id}` | Retrieve an analysis    |
| POST   | `/api/v1/feedback`               | Submit feedback         |
| GET    | `/api/v1/health`                 | Health check            |
| GET    | `/api/v1/models`                 | Retrieve model metadata |

---

# 21. Report Response Shape

```json
{
  "analysis_id": "uuid",
  "model_version": "baseline-0.1.0",
  "scores": {
    "overall_uncertainty": 78,
    "technical_feasibility": 42,
    "problem_reality": 64,
    "monetization_clarity": 29,
    "validation_readiness": 18
  },
  "confidence": {
    "overall": "low"
  },
  "detected_patterns": [
    "low_validation_evidence",
    "unclear_monetization"
  ],
  "recommendations": [
    "Interview potential customers",
    "Test willingness to pay before building"
  ],
  "roast": {
    "intensity": "brutal",
    "text": "Your pitch deck has more certainty than your customer base."
  }
}
```

---

# 22. Success Metrics

## Product Metrics

* Completed analyses.
* Report completion rate.
* Feedback response rate.
* Share rate.
* Repeat usage.
* Simulator usage after launch.

## ML Metrics

* Regression MAE/RMSE.
* Classification F1-score.
* Calibration.
* Human-model agreement.
* Performance by startup category.
* Annotation consistency.

## Quality Metrics

* Roast grounding rate.
* Hallucination/error reports.
* Recommendation usefulness.
* User-reported clarity.

---

# 23. Development Roadmap

## Phase 0: Research

* [ ] Finalize rubric.
* [ ] Define labels.
* [ ] Collect initial examples.
* [ ] Design annotation workflow.
* [ ] Document data limitations.

## Phase 1: ML Baseline

* [ ] Build dataset loader.
* [ ] Implement preprocessing.
* [ ] Train dummy baselines.
* [ ] Train Ridge Regression.
* [ ] Train Logistic Regression.
* [ ] Evaluate using cross-validation.
* [ ] Create model cards.

## Phase 2: Backend

* [ ] Build FastAPI service.
* [ ] Add schemas.
* [ ] Integrate model inference.
* [ ] Add persistence.
* [ ] Add model versioning.

## Phase 3: Roast Engine

* [ ] Create grounded prompt builder.
* [ ] Add roast intensity.
* [ ] Add validation and fallback behavior.
* [ ] Test against adversarial inputs.

## Phase 4: Frontend

* [ ] Build landing page.
* [ ] Build idea submission flow.
* [ ] Build loading experience.
* [ ] Build results dashboard.
* [ ] Add visual score breakdown.
* [ ] Add shareable report cards.

## Phase 5: Feedback and Iteration

* [ ] Collect feedback.
* [ ] Analyze errors.
* [ ] Expand dataset.
* [ ] Add Delulu Simulator.
* [ ] Retrain models.

---

# 24. Risks and Mitigations

## Risk: Arbitrary Scoring

**Mitigation:** Use documented rubrics, human labels, and model evaluation.

## Risk: Subjective Labels

**Mitigation:** Multiple annotators, confidence scores, and disagreement analysis.

## Risk: False Authority

**Mitigation:** Clearly label outputs as estimates and uncertainty assessments.

## Risk: LLM Hallucinations

**Mitigation:** Ground generation in structured findings and validate output.

## Risk: Dataset Bias

**Mitigation:** Include varied industries, business models, and founder backgrounds.

## Risk: Comedy Becoming Offensive

**Mitigation:** Roast ideas and assumptions, not protected traits or personal identity.

---

# 25. MVP Definition of Done

The MVP is complete when:

* A user can submit a startup idea.
* The system validates and stores the submission.
* A trained baseline model produces structured predictions.
* Predictions are versioned and reproducible.
* The system generates grounded recommendations.
* An LLM produces a funny but constructive roast.
* The frontend displays a complete report.
* Users can submit feedback.
* The repository includes setup instructions, experiments, evaluation results, and limitations.

---

# 26. Open Questions

* Which evaluation dimensions should be human-labeled first?
* Should the first model use only structured features or include text embeddings?
* How many annotators are needed per idea?
* Should scores be normalized by startup category?
* Should users be allowed to submit anonymously?
* What is the minimum evidence required to classify an idea as MVP-ready?
* How should confidence be communicated to nontechnical users?
