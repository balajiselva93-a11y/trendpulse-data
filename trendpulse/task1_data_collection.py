import requests
import os
import json
import time
from datetime import datetime

# 🔹 Categories
CATEGORIES = {
    "technology": ["ai", "software", "tech", "code", "computer", "data", "cloud", "api", "gpu", "llm"],
    "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global"],
    "sports": ["nfl", "nba", "fifa", "sport", "game", "team", "player", "league", "championship"],
    "science": ["research", "study", "space", "physics", "biology", "discovery", "nasa", "genome"],
    "entertainment": ["movie", "film", "music", "netflix", "game", "book", "show", "award", "streaming"]
}

MAX_PER_CATEGORY = 25

headers = {
    "User-Agent": "TrendPulse/1.0"
}

# 🔹 Create data folder if not exists
if not os.path.exists("data"):
    os.makedirs("data")

# 🔹 Step 1: Fetch story IDs
ids_url = "https://hacker-news.firebaseio.com/v0/topstories.json"
story_ids = requests.get(ids_url).json()

# 🔹 Storage
categorized = {cat: [] for cat in CATEGORIES}

def assign_category(title):
    title_lower = title.lower()
    for category, keywords in CATEGORIES.items():
        for keyword in keywords:
            if keyword in title_lower:
                return category
    return None

# 🔹 Step 2: Fetch details
for story_id in story_ids:
    url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
    res = requests.get(url, headers=headers)

    if res.status_code != 200:
        continue

    data = res.json()
    if not data or "title" not in data:
        continue

    category = assign_category(data["title"])

    if category and len(categorized[category]) < MAX_PER_CATEGORY:
        categorized[category].append({
            "post_id": data.get("id"),
            "title": data.get("title"),
            "category": category,
            "score": data.get("score"),
            "num_comments": data.get("descendants"),
            "author": data.get("by"),
            "collected_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

    # Stop when all categories filled
    if all(len(v) >= MAX_PER_CATEGORY for v in categorized.values()):
        break

    time.sleep(0.05)

# 🔹 Flatten data
final_data = []
for cat_list in categorized.values():
    final_data.extend(cat_list)

# 🔹 File name with date
date_str = datetime.now().strftime("%Y%m%d")
file_path = f"data/trends_{date_str}.json"

# 🔹 Save JSON
with open(file_path, "w", encoding="utf-8") as f:
    json.dump(final_data, f, indent=4)

# 🔹 Print result
print(f"Collected {len(final_data)} stories. Saved to {file_path}")