## Keyword Scanner Web Application

This repository contains a **very simply** amateur-ish Flask-based web application that scans uploaded files for specific keywords. The app extracts text from various file types (TXT, PDF, Word, and Excel), searches for matches based on a user-provided keyword list (stored in `dei_terms.txt`), and generates summary and excerpt Excel reports.

## Features

- **Multi-Format File Processing:**  
  Supports text files (`.txt`), PDFs (`.pdf`), Word documents (`.docx`), and Excel files (`.xls`/`.xlsx`).

- **Keyword Extraction & Analysis:**  
  - Loads keywords from a dedicated file (`dei_terms.txt`).  
  - Extracts sentences containing keywords.  
  - Performs text Normalization for Keyword Matching:
  - Provides a frequency count of keyword occurrences.
  - Provides excerpts 

- **User-Friendly Interface:**  
  - Drag & drop or manual file upload.  
  - Progress bar and real-time UI updates during processing.
  - Downloadable results for keyword matches and corresponding excerpts.

- **Report Generation:**  
  Generates two Excel reports:
  - **Keyword Match:** For each file, the code creates a summary that includes the file name, the matched keywords, the total count of matched keywords, and a dictionary of each keyword’s frequency.
  - **Excerpts:** It collects all sentences where keywords were found.


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

## License

This project is licensed under Creative Commons Attribution-NonCommercial-ShareAlike (CC BY-NC-SA) license.
