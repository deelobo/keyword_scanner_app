## Keyword Scanner

[https://keyword-scanner-app.onrender.com](https://keyword-scanner-app.onrender.com)

This repository contains a simple web application built with Python and Flask to automate the scanning of documents for approx. **700 keywords and phrases** identified as "DEI terms" in the 2024 report titled "DEI: Division. Extremism. Ideology: How the Biden-Harris NSF Politicized Science" by the U.S. Senate Committee on Commerce, Science, and Transportation.

**What does the app do?** It extracts text from documents, searches for keyword matches, and generates keyword match summary and excerpt reports in a spreadsheet format. For more details, please see the [What the App Does and Limitations](https://github.com/deelobo/keyword_scanner_app#what-the-app-does-and-limitations) section below.

**Important notes (please read it!)**:

1. **First things first**: I *do not* endorse the political viewpoints, ideologies, and conclusions presented in the report.

2. The deployed app (link above) is running on a free instance (a free-tier plan provided by the hosting site), which comes with limitations:
   - 🐢 **Slow performance:** The app may take time to load and process files.
   - ⏳ **Automatic spin-down:** The server will go offline after 15 minutes of inactivity. Bringing it back online may take about a minute.
   - 🚫  **Usage limits:** It may stop working entirely if the monthly usage limit has been reached.

3. ⚠️ This application **was not** designed or tested for production or commercial use. It is an experimental project and **contributions to improve it are welcome and appreciated**! You can help improve this app by sending pull requests through GitHub!

## Usage

### 📤 Upload Documents
- Use the drag & drop area or click to select files. **Multiple files can be uploaded at once**.
- Supported file formats include text files (.txt, .docx), PDFs (.pdf), and spreadsheet files (.csv, .xls, .xlsx).
  **Note**: Scanned PDFs and image files are not supported at this time.

### 🔍 Scan Documents
- Click the "scan" button to begin processing. 
- A "scanning for matches" message will appear while the app processes your documents.

### 📥 Download Reports
- Once processing is complete, download the generated reports by clicking on the "keyword match" and "excerpts" buttons. 

### 🔄 New Search
- Use the "new search" button to reset the interface and start over.


## What the App Does and Limitations

The app uses Python’s regular expression library (`re`) to perform exact keyword matching. Here’s how it works:

#### 📝 Text Extraction and Sentence Segmentation
The app extracts text from documents and split it into sentences using a regular expression designed to detect sentence boundaries (e.g., periods, question marks) while minimizing false splits (e.g., avoiding splits on abbreviations like "U.S." or "Dr.").

#### 🔍 Case-Insensitive Search with Whole-Word Matching
Each sentence is scanned for the target keywords using a regular expression with word boundary markers (\b). The search is case-insensitive to ensure consistent matching regardless of text formatting.

#### 📊 Keyword Extraction and Counting
When a keyword is found, the app records the occurrence, extracts the sentence where the keywords appear, and updates a frequency count for each matched term.

#### 📝 Report Generation
After processing the text, the app produces two **.csv** reports:
- Keyword match summary: Lists the matched terms, the total number of matched terms, and the frequency of each term.
- Excerpts: Contains the matched keywords paired with the sentences in which they appear.


### Some Limitations (Others Might Exist!)

- **Scale and Performance**: The app was designed for small-scale, non-production use and handles small documents and files well (e.g., 2–4 pages, files with a few MB in size). Processing large text files or spreadsheets may result in slower performance or failure.
- **Exact Term Matching Only**: The app detects only the exact terms as they appear in the provided list. It does not account for typographical errors or context-dependent meanings.
- **No OCR Support**: The code extracts text only from documents with selectable/searchable text. For scanned images or PDFs without embedded text, an OCR solution would need to be integrated.


## Development and deployment

The application is developed in Python using Flask, with the keyword list provided in `dei_terms.txt` and dependencies managed via `requirements.txt`. The structure is designed to keep uploads and generated reports separate, with dedicated folders (uploads/ and results/), while the user interface is maintained in the templates/ and static/ directories.

### Prerequisites

- Python 3.6 or higher
- Python libraries
  
```
   - Flask==2.2.3
   - Werkzeug==2.2.3
   - gunicorn==23.0.0
   - pandas==2.2.1
   - PyMuPDF==1.24.10
   - python-docx==1.1.2
   - openpyxl==3.1.2
```

### Deployment

**For local deployment**, install dependencies and run the application.

```bash
pip install -r requirements.txt
```
  
```bash
python app.py
```

**For cloud deployment**, see [Render Tutorial](https://render.com/docs/your-first-deploy)
  
  
## References and Links

- U.S. Senate Committee on Commerce, Science & Transportation Report (2024). **DEI: Division. Extremism. Ideology: How the Biden-Harris NSF Politicized Science**. Available at https://www.commerce.senate.gov/services/files/4BD2D522-2092-4246-91A5-58EEF99750BC
  
- [Discover Flask](https://discoverflask.com)
- [Render](https://render.com)


## License
This project is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike (CC BY-NC-SA) license.