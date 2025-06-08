#!/bin/bash

echo "Step 1: Converting CSV to XML"
cd scripts
python3 convert.py
cd ..

echo "Step 2: Validating XML"
java -jar tool/jing.jar schema/article.rng output/articles.xml

echo "Step 3: Inserting XML into MongoDB"
cd scripts
python3 transfer.py
cd ..

echo "Step 4: Exporting MongoDB data to JSON"
cd scripts
python3 export.py
cd ..

echo "Step 5: Launching data at http://localhost:8000"
cd viewer
python3 -m http.server 8000
