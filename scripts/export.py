import pymongo
import json
import os

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["FakeNewsDB"]
collection = db["Articles"]

# Fetch all articles
all_articles = list(collection.find())

# Clean: Remove _id fields for frontend compatibility
for article in all_articles:
    article.pop("_id", None)

# Output path
output_path = os.path.join("..", "viewer", "articles_sample.json")

# Write to JSON file
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(all_articles, f, indent=2, ensure_ascii=False)

print(f"Exported {len(all_articles)} articles to {output_path}")
