## Keyword Scanner for "DEI" terms

The Keyword Scanner is a simple web application built with Python and Flask to automate the scanning of documents for keywords and phrases listed in the Appendix B of the U.S. Senate Committee on Commerce, Science & Transportation's report titled "DEI: Division. Extremism. Ideology: How the Biden-Harris NSF Politicized Science" (2024).

The list comprises approximately 700 keywords and phrases labeled as "DEI" terms, divided into five categories: (socio-economic) status, social justice, gender, race, and environmental justice (including climate change).

The application extracts text from various file types (TXT, PDF, Word, and Excel), searches for keyword matches based on the provided list, and generates comprehensive summary and excerpt reports in Excel format. For more details, please see the "What the App Does and Limitations" section below.

**Important note**: The developer *does not* endorse the political viewpoints, ideologies, and conclusions presented in the report.

**Link to web application:**
https://keyword-scanner-app.onrender.com/

## Features

- **Multi-Format File Processing:**  
  - Supports text files (`.txt`/`.docx`), PDFs (`.pdf`), and spreadsheet files (`.csv`/`.xls`/`.xlsx`).
  - **DO NOT** support scanned or image-based PDFs (see other limitations below)

- **Keyword Extraction & Analysis:**  
  - Loads keywords from a dedicated file (`dei_terms.txt`).  
  - Performs text normalization to enhance the accuracy of keyword matching.
  - Extracts sentences containing matched keywords.  
  - Provides a frequency count of keyword occurrences.
  - Provides excerpts

- **User-Friendly Interface:**  
  - Drag & drop or manual file upload.  
  - Downloadable results for keyword matches and corresponding excerpts.

- **Report Generation:**  
  Generates two Excel reports:
  - **Keyword Match:** For each file, the code creates a summary that includes the file name, the matched keywords, the total count of matched keywords, and a dictionary of each keyword’s frequency.
  - **Excerpts:** It collects all sentences where keywords were found.

- Read section methods and pipeline for details of  application 
- 
## Prerequisites

- Python 3.6 or higher
- Install Dependencies

```bash
pip install -r requirements.txt
```

- Create a `requirements.txt` file that includes all the libraries

   - Flask==2.2.3
   - Werkzeug==2.2.3
   - gunicorn==23.0.0
   - pandas==2.2.1
   - PyMuPDF==1.24.10
   - python-docx==1.1.2
   - openpyxl==3.1.2


- Create a file named `dei_terms.txt` in the project root and add the keywords (one per line) you want to scan for.


### File Structure
```
keyword-scanner/
├── app.py                 # Main Flask application
├── dei_terms.txt          # File containing keywords (one per line)
├── requirements.txt       # List of Python dependencies
├── uploads/               # Directory where uploaded files are saved
├── results/               # Directory for generated Excel reports
├── templates/
│   └── index.html         # HTML template for the web interface
└── static/
    └── style.css          # CSS styles for the UI (and any other static assets)
```
## Deployment

This application is designed and optimized to run on [Render](https://render.com). When deploying on Render, make sure to configure your environment variables and file paths as needed.

## Usage

#### Upload Files

Use the drag & drop area or click to select files. Multiple files can be uploaded at once.

#### Scan Files

Click the "scan" button to begin processing. A progress bar and a "processing" message will appear.

#### Download Reports

Once processing is complete, download the generated summary and excerpt reports using the provided links.

#### New Search

Use the "new search" button to reset the interface and start over.

### What the App Does and Limitations
The application uses Python’s regular expression library (re) to perform keyword matching. Here’s how it works:
#### Text Normalization:
The input text is first normalized by splitting it into sentences using a regular expression designed to detect sentence boundaries while minimizing false splits.
#### Whole-Word Matching:
Each sentence is scanned for the target keywords using a regular expression with word boundary markers (\b). This ensures that only whole words are matched, avoiding partial matches within longer words.
#### Case-Insensitive Search:
The search is case-insensitive, converting the text to lowercase (or using a case-insensitive flag) to ensure consistent matching regardless of text formatting.
#### Extraction and Counting:
When a keyword is found, the application records the occurrence, extracts the complete sentence for context, and updates a frequency count for each matched term.

### Some limitations (other might exist!)

- **Scale and Performance**: The app is designed for small-scale deployments and handles smaller files efficiently. Processing very large text files or spreadsheets may result in slower performance or even failure.
- **Exact Term Matching Only**: The app only detects the exact terms listed in the keyword file. It does not evaluate whether the terms are used in a context related to diversity, equity, or inclusion.
- **No OCR Support**: The code extracts text only from documents with selectable text. For scanned images or PDFs without embedded text, an OCR solution would need to be integrated.
- **Potential for Undetected Terms**: The app uses regular expressions that treats letters, digits, and underscores as word characters. Therefore, the text "equity-based" would not be flagged.

### Links
https://discoverflask.com
https://render.com
U.S. Senate Committee on Commerce, Science & Transportation. (2024.). DEI: Division. Extremism. Ideology: How the Biden-Harris NSF politicized science [Report]. Retrieved from https://www.commerce.senate.gov/services/files/4BD2D522-2092-4246-91A5-58EEF99750BC

## License
This project is licensed under Creative Commons Attribution-NonCommercial-ShareAlike (CC BY-NC-SA) license.
