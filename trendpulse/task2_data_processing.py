import pandas as pd

# 🔹 File path (update date if needed)
file_path = "data/trends_20260410.json"

# 🔹 Load JSON into DataFrame
df = pd.read_json(file_path)
# 1️⃣ Remove duplicates
df = df.drop_duplicates(subset="post_id")
print(f"After removing duplicates: {len(df)}")

# 2️⃣ Remove nulls
df = df.dropna(subset=["post_id", "title", "score"])
print(f"After removing nulls: {len(df)}")

# 3️⃣ Fix data types
df["score"] = pd.to_numeric(df["score"], errors="coerce").fillna(0).astype(int)
df["num_comments"] = pd.to_numeric(df["num_comments"], errors="coerce").fillna(0).astype(int)

# 4️⃣ Remove low score (<5)
df = df[df["score"] >= 5]
print(f"After removing low scores: {len(df)}")

# 5️⃣ Clean title whitespace
df["title"] = df["title"].str.strip()

# 🔹 Save to CSV
output_path = "data/trends_clean.csv"
df.to_csv(output_path, index=False)

print(f"Saved {len(df)} cleaned stories to {output_path}")

# 🔹 Category summary
print("\nStories per category:")
print(df["category"].value_counts())