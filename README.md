## 'DEI' Keyword Scanner

This repository contains a simple web application built with Python and Flask to automate the scanning of documents for approx. **700 keywords and phrases** defined as "DEI" terms in the 2024 report titled "DEI: Division. Extremism. Ideology: How the Biden-Harris NSF Politicized Science" by the U.S. Senate Committee on Commerce, Science, and Transportation.

**What does the app do?** It extracts text from various file types, searches for keyword matches, and generates keyword match summary and excerpt reports in a spreadsheet format. For more details, please see the "What the App Does and Limitations" section below.

**Link to web application:**
[https://keyword-scanner-app.onrender.com](https://keyword-scanner-app.onrender.com)


**Important notes (read it!)**:

1. **First things first**: I *do not* endorse the political viewpoints, ideologies, and conclusions presented in the report.

2. If using the link above: This app is running on a free-tier plan (free instance provided by the hosting site - Thanks,Render!), which comes with limitations:
   - 🐢 It runs slowly.
   - ⏳ It will automatically spin down after 15 minutes of inactivity. Bringing the server back online may take about a minute.
   - 🚫 It may stop working entirely if the monthly usage limit has been reached.
   - 🔧 As of now, I don't plan to upgrade the hosting instance. I **highly** encourage you to fork this repository and create your own instance on Render. Here is the tutorial: [Render Tutorial](https://render.com/docs/free)

3. ⚠️ This application **was not** designed or tested for production use (that is, for continued or mass use). It is an experimental project, and <span style="color: purple;">**I welcome your contributions to improve it!**</span>  


## Features

✨ **Easy File Upload and Multi-Format Support**:
- Simple, Decluttered UI: A clean and intuitive interface.
- Flexible Upload Options: Upload files via drag-and-drop or manual selection.
- Multi-Format Support: Handles text files (.txt, .docx), PDFs (.pdf), and spreadsheet files (.csv, .xls, .xlsx).
  - Note: Scanned or image-based PDFs and image files are not supported at this time.

🔍 **Keyword Extraction & Reporting**:
- Scans documents for "DEI" terms as defined in the 2024 report "DEI: Division. Extremism. Ideology: How the Biden-Harris NSF Politicized Science" by the U.S. Senate Committee on Commerce, Science, and Transportation.
- Generates downloadable spreadsheets that include:
  - Matched terms.
  - Total number of matches.
  - Frequency of each term.
  - Excerpts showing the context of each match.

## Prerequisites

- Python 3.6 or higher
- Create a `requirements.txt` file that includes all the libraries
  
```
   - Flask==2.2.3
   - Werkzeug==2.2.3
   - gunicorn==23.0.0
   - pandas==2.2.1
   - PyMuPDF==1.24.10
   - python-docx==1.1.2
   - openpyxl==3.1.2
```
- Install Dependencies
  
```bash
pip install -r requirements.txt
```

- Create the file `dei_terms.txt` that includes the keywords (one per line) you want to scan for.

- Set up the folder structure as below

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

This application is designed and optimized to run on [Render](https://render.com). When deploying on Render, make sure to configure your environment variables as needed.

## Usage

### 📤 Upload Files
- Use the drag & drop area or click to select files. Multiple files can be uploaded at once.

### 🔍 Scan Files
- Click the "scan" button to begin processing. A progress bar and a "processing" message will appear.

### 📥 Download Reports
- Once processing is complete, download the generated summary and excerpt reports using the provided links.

### 🔄 New Search
- Use the "new search" button to reset the interface and start over.


## What the App Does and Limitations

The app uses Python’s regular expression library (`re`) to perform exact keyword matching. Here’s how it works:

#### 📝 Text Normalization
The input text is first normalized by splitting it into sentences using a regular expression designed to detect sentence boundaries while minimizing false splits.

#### 🔍 Whole-Word Matching
Each sentence is scanned for the target keywords using a regular expression with word boundary markers (`\b`). This ensures that only whole words are matched, avoiding partial matches within longer words.

#### 🔠 Case-Insensitive Search
The search is case-insensitive to ensure consistent matching regardless of text formatting.

#### 📊 Extraction and Counting
When a keyword is found, the application records the occurrence, extracts the complete sentence for context, and updates a frequency count for each matched term.

### Some Limitations (Others Might Exist!)

- **Scale and Performance**: The app was designed for small-scale deployments (a personal project) and handles smaller files well (e.g., 2–4 pages, files with a few MB in size). Processing large text files or spreadsheets may result in slower performance or failure.
- **Exact Term Matching Only**: The app only detects the exact terms listed in the keyword file. It does not evaluate whether the terms are used in a context related to diversity, equity, or inclusion.
- **No OCR Support**: The code extracts text only from documents with selectable text. For scanned images or PDFs without embedded text, an OCR solution would need to be integrated.

### References and Links

- U.S. Senate Committee on Commerce, Science & Transportation Report (2024). **DEI: Division. Extremism. Ideology: How the Biden-Harris NSF Politicized Science**. Available at https://www.commerce.senate.gov/services/files/4BD2D522-2092-4246-91A5-58EEF99750BC
- [Discover Flask](https://discoverflask.com)
- [Render](https://render.com)


## License
This project is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike (CC BY-NC-SA) license.