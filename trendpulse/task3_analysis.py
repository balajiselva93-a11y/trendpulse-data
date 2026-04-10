import pandas as pd
import numpy as np

# =========================
# 1 — Load and Explore
# =========================
file_path = "data/trends_clean.csv"
df = pd.read_csv(file_path)

print("First 5 rows:")
print(df.head())

print("\nShape (rows, columns):")
print(df.shape)

avg_score = df["score"].mean()
avg_comments = df["num_comments"].mean()

print("\nAverage score:", round(avg_score, 2))
print("Average num_comments:", round(avg_comments, 2))


# =========================
# 2 — NumPy Analysis
# =========================
scores = df["score"].to_numpy()
comments = df["num_comments"].to_numpy()

print("\nScore Statistics:")
print("Mean:", round(np.mean(scores), 2))
print("Median:", np.median(scores))
print("Std Dev:", round(np.std(scores), 2))

print("\nScore Range:")
print("Highest:", np.max(scores))
print("Lowest:", np.min(scores))

top_category = df["category"].value_counts().idxmax()
print("\nCategory with most stories:", top_category)

max_comments_index = np.argmax(comments)
print("\nMost commented story:")
print("Title:", df.iloc[max_comments_index]["title"])
print("Comments:", df.iloc[max_comments_index]["num_comments"])


# =========================
# 3 — Add New Columns
# =========================

# Engagement = comments per upvote
df["engagement"] = df["num_comments"] / (df["score"] + 1)

# Popular if score > average score
df["is_popular"] = df["score"] > avg_score


# =========================
# 4 — Save Result
# =========================
output_path = "data/trends_analysed.csv"
df.to_csv(output_path, index=False)

print(f"\nSaved analysed data to {output_path} with {len(df)} rows.")