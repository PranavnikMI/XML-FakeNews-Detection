import csv
import os
import xml.etree.ElementTree as ET
from datetime import datetime

# Function to indent the XML for good-printing
def indent(elem, level=0):
    i = "\n" + level * "  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        for child in elem:
            indent(child, level + 1)
        if not child.tail or not child.tail.strip():
            child.tail = i
    if level and (not elem.tail or not elem.tail.strip()):
        elem.tail = i
    return elem

# Input and output file paths
fake_file = "../data/Fake.csv"
true_file = "../data/True.csv"
output_file = "../output/articles.xml"

# Ensure output directory exists
os.makedirs("../output", exist_ok=True)

# Create root <articles> element
articles_root = ET.Element("articles")

# Function to process each CSV file
def process_csv(file_path, label_value):
    with open(file_path, newline='', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for idx, row in enumerate(reader):
            article = ET.Element("article")

            ET.SubElement(article, "headline").text = row["title"]
            ET.SubElement(article, "body").text = row["text"]
            ET.SubElement(article, "label").text = label_value
            ET.SubElement(article, "subject").text = row["subject"]

            # Handle date (with missing or bad format support)
            raw_date = row["date"].strip()
            if raw_date:
                try:
                    parsed_date = datetime.strptime(raw_date, "%B %d, %Y")
                    formatted_date = parsed_date.strftime("%Y-%m-%d")
                except Exception:
                    formatted_date = "unknown"
            else:
                formatted_date = "unknown"

            ET.SubElement(article, "date").text = formatted_date

            # Append to root
            articles_root.append(article)

# Process both fake and real news files
process_csv(fake_file, "fake")
process_csv(true_file, "real")

# Indent the tree nicely
indent(articles_root)

# Save to output XML file
tree = ET.ElementTree(articles_root)
tree.write(output_file, encoding="utf-8", xml_declaration=True)

print(f"XML file created at : {output_file}")
