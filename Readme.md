# DeluluScore

<p align="center">
  <img src="https://img.shields.io/badge/status-prototype-orange" alt="Status: Prototype" />
  <img src="https://img.shields.io/badge/python-3.12+-blue" alt="Python 3.12+" />
  <img src="https://img.shields.io/badge/react-vite-61DAFB" alt="React + Vite" />
  <img src="https://img.shields.io/badge/fastapi-0.115+-green" alt="FastAPI" />
  <img src="https://img.shields.io/badge/ml-scikit_learn-purple" alt="Scikit-learn" />
</p>

> Every startup idea deserves a reality check.

DeluluScore is a comedy-first startup evaluation product that helps founders stress-test their assumptions before turning a pitch into a product roadmap. It blends structured scoring, lightweight ML, market research hooks, and a roast engine that is more useful than a motivational quote.

Built for the moment when a founder says, “This is obviously a huge opportunity,” and the product replies, “Great. Let’s test the assumptions before we deploy Kubernetes.”

---

## Why it exists

Most early startup ideas sound compelling until someone asks a few uncomfortable questions:

- Who exactly is the customer?
- What problem are they already paying to solve?
- Why is this better than the status quo?
- What is the smallest version we can validate?
- What would make this fail in six weeks?

DeluluScore turns those questions into a structured score and a grounded recommendation.

---

## What the product does

- Scores startup ideas across product, technical, market, and monetization dimensions
- Surfaces assumption-heavy areas instead of pretending to know the future
- Generates a short, practical recommendation for the next validation step
- Delivers a deliberately funny roast that is still grounded in the actual score
- Gives founders a more honest way to think before they build

---

## Tech stack

<div align="center">
  <table>
    <tr>
      <td align="center"><strong>Frontend</strong><br />React · Vite · CSS<br /><em>polished UX</em></td>
      <td align="center"><strong>API</strong><br />FastAPI · Pydantic · Uvicorn<br /><em>robust service layer</em></td>
      <td align="center"><strong>ML</strong><br />Python · scikit-learn · Pandas<br /><em>signal + scoring</em></td>
      <td align="center"><strong>Data & Ops</strong><br />PostgreSQL · Docker · GitHub Actions<br /><em>deployable workflow</em></td>
    </tr>
  </table>
</div>

---

## System flow

```text
Startup idea
   ↓
Structured evaluation
   ↓
Risk/assumption extraction
   ↓
ML + rule-based scoring
   ↓
Actionable recommendation
   ↓
Grounded roast + final report
```

The scoring layer stays honest: it explains uncertainty, not destiny.

---

## Project structure

```text
deluluscore/
├── apps/
│   ├── web/                 # React + Vite frontend
│   └── api/                 # FastAPI service layer
├── ml/
│   ├── src/
│   ├── models/
│   └── notebooks/
├── docs/
├── README.md
├── pyproject.toml
├── requirements.txt
├── LICENSE
└── .env.example
```

---

## Quick start

### 1) Install Python dependencies

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2) Start the API

```bash
.venv/bin/python -m uvicorn apps.api.main:app --reload --port 8000
```

### 3) Start the frontend

```bash
cd apps/web
npm install
npm run dev
```

Then open:

```text
http://127.0.0.1:5173
```

---

## Current status

This project is currently a strong prototype with:

- a clean evaluation flow
- a polished browser-based experience
- a structured scoring model and recommendation layer
- a product tone that favors honesty over hype

It is intentionally designed to be playful without being fake.

---

## Roadmap

- [ ] finalize the evaluation rubric
- [ ] improve ML signal quality
- [ ] integrate stronger market intelligence
- [ ] add richer report sharing and export flows
- [ ] expand dataset quality and labeling processes
- [ ] ship production-ready deployment workflows

---

## License

License is still being finalized for the repository.

---

## Author

Built by [Muneer Alam](https://github.com/Muneer320).

A project at the intersection of product sense, machine learning, and the uncomfortable truth that “this seems like a good idea” is not yet evidence.

> Got a startup idea?
>
> Let’s see if it survives the first brutally honest conversation.
