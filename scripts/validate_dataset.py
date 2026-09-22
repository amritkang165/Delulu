import pandas as pd

DATASET_PATH = "ml/data/raw/startup_ideas.csv"

df = pd.read_csv(DATASET_PATH)

print("Dataset shape:", df.shape)
print("\nColumns:")
print(df.columns.tolist())

print("\nMissing values:")
print(df.isnull().sum())

score_columns = [
    "problem_clarity",
    "customer_urgency",
    "technical_complexity",
    "monetization_clarity",
    "acquisition_difficulty",
    "competition_level",
    "validation_evidence",
    "mvp_complexity",
    "overall_uncertainty",
]

print("\nScore validation:")

for column in score_columns:
    invalid = ~df[column].between(1, 10)

    if invalid.any():
        print(f"❌ {column}: invalid values found")
    else:
        print(f"✅ {column}: all values valid")

print("\nDuplicate idea IDs:", df["idea_id"].duplicated().sum())
print("Duplicate startup names:", df["startup_name"].duplicated().sum())

print("\nValidation readiness values:")
print(df["validation_readiness"].value_counts())

print("\nStartup archetypes:")
print(df["startup_archetype"].value_counts())

print("\nDataset validation complete.")