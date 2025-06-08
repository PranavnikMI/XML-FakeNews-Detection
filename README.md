# XML-FakeNews-Detection 
This project identifies and classifies fake and real news articles. The process includes converting CSV data into XML, validating it, storing in MongoDB, and viewing the result in a browser.


# Project Folders
1. data/ → Contains original CSV files (Fake.csv and True.csv)
2. output/ → Stores the generated XML file (articles.xml)
3. schema/ → Holds the RelaxNG schema (article.rng)
4. tool/ → Includes jing.jar used for validation
5. scripts/ → Python files to convert, transfer, and export data
6. viewer/ → HTML viewer with search, filter, and full-article display


# Steps to Run the Project
1. Open terminal and go to the main folder:
    cd TTProject
2. Make the run script executable (only once):
    chmod +x run.sh
3. Run the project:
    ./run.sh


# This commands will:
- Convert CSV to XML
- Validate XML using RelaxNG
- Insert into MongoDB
- Export all articles as JSON
- Launch a local HTML viewer


# Tools Used
- Python
- MongoDB
- XML + RelaxNG
- Java (for validation)
- HTML + JavaScript (for frontend)


# Output
- After running, open this in your browser:
    http://localhost:8000
(You can search, filter, sort, and expand articles inside the web viewer.)