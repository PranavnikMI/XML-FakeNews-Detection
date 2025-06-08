import xmltodict
import pymongo
from pymongo.errors import BulkWriteError

# Load the XML
with open("../output/articles.xml", "r", encoding="utf-8") as file:
    xml_content = file.read()

# Parse XML
data_dict = xmltodict.parse(xml_content)
articles = data_dict["articles"]["article"]
if isinstance(articles, dict):
    articles = [articles]

# Clean each article
def clean_article(article):
    return {
        "headline": str(article.get("headline", ""))[:500],
        "body": str(article.get("body", ""))[:10000],
        "label": str(article.get("label", "")),
        "subject": str(article.get("subject", "")),
        "date": str(article.get("date", "unknown"))
    }

cleaned_articles = [clean_article(a) for a in articles]

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["FakeNewsDB"]          
collection = db["Articles"]

# Insert
collection.delete_many({})

try:
    result = collection.insert_many(cleaned_articles, ordered=False)
    print(f"Inserted {len(result.inserted_ids)} articles into MongoDB")
except BulkWriteError as bwe:
    failed = len(bwe.details.get("writeErrors", []))
    print(f"{failed} failed inserts.")

