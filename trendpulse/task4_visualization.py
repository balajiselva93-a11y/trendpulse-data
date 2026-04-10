import pandas as pd
import matplotlib.pyplot as plt
import os

# =========================
# 1 — Setup
# =========================
file_path = "data/trends_analysed.csv"
df = pd.read_csv(file_path)

# Create outputs folder
if not os.path.exists("outputs"):
    os.makedirs("outputs")

# =========================
# 2 — Chart 1: Top 10 Stories by Score
# =========================
top10 = df.sort_values(by="score", ascending=False).head(10)

# Shorten titles
top10["short_title"] = top10["title"].apply(lambda x: x[:50] + "..." if len(x) > 50 else x)

plt.figure()
plt.barh(top10["short_title"], top10["score"])
plt.xlabel("Score")
plt.ylabel("Story Title")
plt.title("Top 10 Stories by Score")
plt.gca().invert_yaxis()

plt.savefig("outputs/chart1_top_stories.png")
plt.close()

# =========================
# 3 — Chart 2: Stories per Category
# =========================
category_counts = df["category"].value_counts()

plt.figure()
plt.bar(category_counts.index, category_counts.values)
plt.xlabel("Category")
plt.ylabel("Number of Stories")
plt.title("Stories per Category")

plt.savefig("outputs/chart2_categories.png")
plt.close()

# =========================
# 4 — Chart 3: Score vs Comments
# =========================
plt.figure()

# Separate popular vs non-popular
popular = df[df["is_popular"] == True]
not_popular = df[df["is_popular"] == False]

plt.scatter(popular["score"], popular["num_comments"], label="Popular")
plt.scatter(not_popular["score"], not_popular["num_comments"], label="Not Popular")

plt.xlabel("Score")
plt.ylabel("Number of Comments")
plt.title("Score vs Comments")
plt.legend()

plt.savefig("outputs/chart3_scatter.png")
plt.close()

print("✅ All charts saved in outputs/ folder")