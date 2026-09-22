# DeluluScore Labeling Rubric

Version: 0.1.0

All numerical evaluation scores range from 1 to 10.

Scores must be based on the submitted idea and available evidence,
not on personal preference or whether the evaluator likes the idea.

---

## 1. Problem Clarity

How clearly does the idea define a specific, meaningful problem?

| Score | Definition |
|---|---|
| 1–2 | No clear problem; mostly a vague concept |
| 3–4 | Problem exists but is poorly defined |
| 5–6 | Understandable problem with some ambiguity |
| 7–8 | Specific problem affecting an identifiable group |
| 9–10 | Extremely clear, specific, and well-understood problem |

---

## 2. Customer Urgency

How urgently would the target customer want this problem solved?

| Score | Definition |
|---|---|
| 1–2 | Problem is mostly optional or insignificant |
| 3–4 | Mild inconvenience; existing workarounds are sufficient |
| 5–6 | Useful problem but not urgent |
| 7–8 | Frequent or costly problem with clear motivation |
| 9–10 | Critical problem causing significant loss, risk, or pain |

---

## 3. Technical Complexity

How difficult would it be to build the proposed solution?

| Score | Definition |
|---|---|
| 1–2 | Simple application with basic functionality |
| 3–4 | Manageable application using established technologies |
| 5–6 | Multiple integrations or moderately complex systems |
| 7–8 | Advanced infrastructure, difficult engineering, or significant scale |
| 9–10 | Extremely difficult research, hardware, infrastructure, or regulatory engineering |

Higher score means greater technical complexity.

---

## 4. Monetization Clarity

How clearly does the idea explain who pays and why?

| Score | Definition |
|---|---|
| 1–2 | No identifiable payer or revenue mechanism |
| 3–4 | Possible monetization but highly speculative |
| 5–6 | Plausible revenue model without strong evidence |
| 7–8 | Clear payer, pricing logic, and monetization path |
| 9–10 | Strong monetization evidence, such as paying customers or validated willingness to pay |

---

## 5. Customer Acquisition Difficulty

How difficult would it be to consistently acquire customers?

| Score | Definition |
|---|---|
| 1–2 | Clearly identifiable customers with easy access |
| 3–4 | Customers reachable through simple channels |
| 5–6 | Requires meaningful marketing, partnerships, or sales |
| 7–8 | Expensive, competitive, or difficult distribution |
| 9–10 | Extremely difficult access, trust barriers, or long enterprise sales cycles |

Higher score means greater acquisition difficulty.

---

## 6. Competition Level

How much competition exists in the target market?

| Score | Definition |
|---|---|
| 1–2 | Few direct alternatives and limited competition |
| 3–4 | Some alternatives but clear room for differentiation |
| 5–6 | Several competitors with established solutions |
| 7–8 | Crowded market with strong existing players |
| 9–10 | Dominated by powerful incumbents or highly commoditized market |

Competition includes:

- Direct competitors
- Indirect alternatives
- Manual workflows
- Existing internal tools
- Doing nothing

---

## 7. Validation Evidence

How much real-world evidence supports customer demand?

| Score | Definition |
|---|---|
| 1–2 | No interviews, users, prototype, or behavioral evidence |
| 3–4 | Informal opinions or assumptions |
| 5–6 | Some interviews, waitlist signups, or prototype feedback |
| 7–8 | Repeated validation, active users, or strong behavioral evidence |
| 9–10 | Paying customers, repeated purchases, or strong measurable demand |

---

## 8. MVP Complexity

How difficult is it to build the smallest useful version?

| Score | Definition |
|---|---|
| 1–2 | Can be built quickly with a narrow feature set |
| 3–4 | Small product with limited dependencies |
| 5–6 | Requires several components or integrations |
| 7–8 | Requires multiple systems, stakeholders, or complex workflows |
| 9–10 | MVP itself requires major infrastructure, network effects, hardware, or research |

---

# Target Variable Definitions

## Overall Uncertainty

Overall uncertainty measures how many important assumptions remain unproven.

It is not a probability of failure.

| Score | Definition |
|---|---|
| 1–2 | Strong evidence and few major unknowns |
| 3–4 | Some uncertainties but relatively clear execution path |
| 5–6 | Several meaningful assumptions remain unvalidated |
| 7–8 | Many important business or execution risks |
| 9–10 | Idea depends on numerous unproven assumptions |

Consider:

- Problem clarity
- Customer urgency
- Validation evidence
- Monetization clarity
- Acquisition difficulty
- Technical complexity
- MVP complexity
- Competition

---

## Validation Readiness

### Needs Discovery

Use when:

- The problem is unclear
- The customer is poorly defined
- There is little evidence of demand
- The idea is mostly assumption-driven

### Needs Validation

Use when:

- The problem is reasonably clear
- Some evidence exists
- Important assumptions remain untested
- Customer demand or willingness to pay is uncertain

### MVP Ready

Use when:

- The customer and problem are clearly defined
- There is meaningful evidence of demand
- The MVP can be scoped realistically
- The next step is building and measuring usage

---

## Startup Archetypes

Choose the most appropriate primary category:

- SaaS
- Marketplace
- Consumer App
- Developer Tool
- AI Application
- FinTech
- HealthTech
- EdTech
- E-commerce
- D2C
- Hardware
- DeepTech
- Blockchain/Web3
- ClimateTech
- Social Platform
- Other

---

# Annotation Rules

1. Do not assign scores based on whether the idea sounds exciting.
2. Do not reward buzzwords such as AI, blockchain, or Web3.
3. Do not penalize an idea merely because it has competitors.
4. Treat competition as a risk only when it affects differentiation or distribution.
5. Separate technical complexity from business uncertainty.
6. A simple idea with no validation can still have high uncertainty.
7. A technically difficult idea may have lower uncertainty if strong evidence exists.
8. Record explanations for unusual or extreme scores.
9. Mark synthetic data clearly.
10. Never present model predictions as guaranteed outcomes.

---

# Dataset Metadata

Current rubric version: 0.1.0

Initial annotation approach: Human-reviewed

Synthetic examples may be used for pipeline testing but must not be
treated as equivalent to real-world validation evidence.