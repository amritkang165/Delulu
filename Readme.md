# 🦄 DeluluScore

> **Every startup idea deserves a reality check.**

DeluluScore is a comedy-first startup idea analysis engine that combines **classical machine learning, structured evaluation, and AI-generated roasts** to help founders identify weak assumptions before spending weeks building something nobody asked for.

Because sometimes your billion-dollar idea is just a Google Form wearing a blockchain hoodie.

---

## ✨ What It Does

Submit a startup idea and receive a structured reality check covering:

* Problem clarity.
* Technical feasibility.
* Customer acquisition difficulty.
* Monetization uncertainty.
* Competitive pressure.
* Validation readiness.
* MVP complexity.

Then get:

* A transparent uncertainty assessment.
* Detected risk patterns.
* Actionable recommendations.
* A personalized AI-generated roast.
* A report you can share with friends, co-founders, or your brutally honest roommate.

---

## 🎯 The Philosophy

DeluluScore is **not** a magical startup-success predictor.

It does not claim to know whether a startup will succeed or fail.

Instead, it evaluates uncertainty and assumption risk based on the information provided.

A high score means more assumptions need validation—not that the idea is objectively bad.

The system separates:

1. Structured evaluation.
2. ML predictions.
3. Recommendations.
4. AI-generated comedy.

This keeps the product entertaining without turning the ML into decorative theater.

---

## 🔥 Example

### Input

> An AI-powered laundry marketplace for college students using blockchain to optimize washing cycles.

### Possible Findings

* Unclear need for blockchain.
* Two-sided marketplace complexity.
* Low validation evidence.
* Unclear monetization.
* Potentially manageable core problem.

### Roast

> You have designed the infrastructure for 10,000 customers who currently exist only in your imagination. Perhaps interview three of them before deploying Kubernetes.

### Recommendation

Start with a simple marketplace MVP and validate whether students will actually pay.

*Example output is illustrative.*

---

## 🧠 How It Works

```text
Startup Idea
     │
     ▼
Structured Questionnaire
     │
     ▼
Feature Extraction
     │
     ▼
Preprocessing Pipeline
     │
     ▼
ML Prediction Engine
     │
     ▼
Structured Findings
     │
     ├──► Recommendations
     │
     └──► Grounded Roast Prompt
                  │
                  ▼
             LLM Roast
                  │
                  ▼
             Final Report
```

The ML engine produces structured findings first.

The LLM turns those findings into entertaining language.

The LLM does not invent the underlying scores.

---

## 🏗️ Planned Architecture

```text
deluluscore/
├── apps/
│   ├── web/                 # Next.js frontend
│   └── api/                 # FastAPI backend
│
├── ml/
│   ├── data/
│   │   ├── raw/
│   │   └── processed/
│   ├── notebooks/
│   ├── src/
│   │   ├── preprocessing.py
│   │   ├── features.py
│   │   ├── train.py
│   │   ├── evaluate.py
│   │   └── predict.py
│   ├── models/
│   └── requirements.txt
│
├── packages/
│   └── schemas/
│
├── docs/
│   ├── methodology.md
│   ├── labeling-rubric.md
│   └── model-card.md
│
├── scripts/
│   └── seed_dataset.py
│
├── docker-compose.yml
├── README.md
├── PRD.md
└── LICENSE
```

---

## 🛠️ Tech Stack

| Layer               | Technology                        |
| ------------------- | --------------------------------- |
| Frontend            | Next.js, TypeScript, Tailwind CSS |
| Backend             | FastAPI, Pydantic                 |
| ML                  | Python, Pandas, Scikit-learn      |
| Database            | PostgreSQL                        |
| Model tracking      | MLflow, planned                   |
| AI roast generation | LLM API                           |
| Deployment          | Vercel + Render/Railway           |

---

## 📊 Machine Learning

The project is designed around real, reproducible ML experimentation.

### Planned Tasks

| Task                        | Approach                                    |
| --------------------------- | ------------------------------------------- |
| Feasibility prediction      | Regression                                  |
| Validation readiness        | Classification                              |
| Startup archetype detection | Multi-class classification                  |
| Uncertainty estimation      | Regression + calibrated interpretation      |
| Feature analysis            | Feature importance and sensitivity analysis |

### Candidate Models

* Dummy baselines.
* Ridge Regression.
* Logistic Regression.
* Random Forest.
* Gradient Boosting.

### Evaluation

Models will be evaluated using:

* Cross-validation.
* Held-out test data.
* MAE.
* RMSE.
* R².
* Precision.
* Recall.
* F1-score.
* Confusion matrices.
* Calibration and error analysis.

> No fake accuracy numbers. Results will be published after experiments are actually run.

---

## 🗂️ Data Strategy

The project will use a combination of:

* Human-labeled startup ideas.
* Public startup descriptions where permitted.
* Synthetic ideas for pipeline testing.
* Optional user feedback.

The initial research target is approximately **100–200 startup ideas**, with multiple evaluations per idea where possible.

Synthetic data will be clearly identified and will not be treated as real-world ground truth.

Every model experiment will document:

* Dataset version.
* Label definitions.
* Preprocessing.
* Train/test strategy.
* Metrics.
* Limitations.

---

## 🎭 Roast Modes

| Mode   | Style                                    |
| ------ | ---------------------------------------- |
| Soft   | Friendly and encouraging                 |
| Honest | Direct and practical                     |
| Brutal | Ruthless toward questionable assumptions |

The system roasts business decisions and product assumptions—not users personally.

---

## 🚀 Roadmap

### Phase 0 — Research

* [ ] Finalize evaluation rubric.
* [ ] Define prediction targets.
* [ ] Design annotation workflow.
* [ ] Collect initial examples.

### Phase 1 — ML Baseline

* [ ] Build dataset pipeline.
* [ ] Implement preprocessing.
* [ ] Train dummy baselines.
* [ ] Train Ridge Regression.
* [ ] Train Logistic Regression.
* [ ] Evaluate and document results.

### Phase 2 — Backend

* [ ] Build FastAPI service.
* [ ] Add request validation.
* [ ] Integrate model inference.
* [ ] Add PostgreSQL persistence.
* [ ] Add model versioning.

### Phase 3 — Roast Engine

* [ ] Build grounded prompt templates.
* [ ] Add roast intensity.
* [ ] Add output validation.
* [ ] Add fallback behavior.

### Phase 4 — Frontend

* [ ] Build landing page.
* [ ] Build idea submission flow.
* [ ] Build loading experience.
* [ ] Build results dashboard.
* [ ] Add shareable report cards.

### Phase 5 — Iteration

* [ ] Collect user feedback.
* [ ] Analyze model errors.
* [ ] Expand dataset.
* [ ] Add Delulu Simulator.
* [ ] Retrain and compare models.

---

## 🧪 Example Evaluation Dimensions

| Dimension                | What It Measures                    |
| ------------------------ | ----------------------------------- |
| Problem Reality          | Is there a meaningful problem?      |
| Technical Feasibility    | Can the MVP realistically be built? |
| Acquisition Difficulty   | Can the founder reach users?        |
| Monetization Uncertainty | Is there a plausible revenue path?  |
| Competitive Pressure     | How difficult is differentiation?   |
| Validation Readiness     | What evidence supports the idea?    |
| MVP Complexity           | How much must be built initially?   |

---

## ⚠️ Limitations

DeluluScore is an experimental decision-support tool.

Its outputs may be affected by:

* Subjective human labels.
* Dataset bias.
* Missing information.
* Industry differences.
* Model limitations.
* Uncertain market conditions.

A score is an estimate, not a verdict.

The product is not financial, legal, investment, or professional business advice.

---

## 🤝 Contributing

Contributions are welcome, especially in:

* Dataset design.
* Evaluation rubrics.
* ML experimentation.
* Feature engineering.
* Frontend design.
* Roast templates.
* Documentation.
* Testing.

Before contributing model improvements, please document:

1. What changed.
2. Why it changed.
3. What data was used.
4. Which metrics improved or worsened.
5. Any new limitations.

---

## 📜 License

License: To be decided.

---

## 👨‍💻 Author

Built by [Muneer Alam](https://github.com/Muneer320).

A project exploring the intersection of **machine learning, product thinking, and unnecessarily honest feedback**.

---

> Got a billion-dollar idea?
>
> Let's find out if it's worth more than the domain name.
