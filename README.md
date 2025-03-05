## Keyword Scanner

This repository contains a simple web application built with Python and Flask to automate the scanning of documents for approx. **700 keywords and phrases** listed in Appendix B of the 2024 report *"DEI: Division. Extremism. Ideology: How the Biden-Harris NSF Politicized Science"* by the U.S. Senate Committee on Commerce, Science, and Transportation.

**Important notes (please read it!)**:

1. **First things first**: I ***do not*** endorse the political viewpoints, ideologies, and conclusions presented in the report. I strongly urge you **not** to use this tool on documents not written by you or for which you do not have explicit permission from the author(s).

2. The deployed app is running on a free instance (a free-tier plan provided by the hosting site), which comes with limitations:
   - 🐢 **Slow performance:** The app may take time to load and process files.
   - ⏳ **Automatic spin-down:** The server will go offline after 15 minutes of inactivity. Bringing it back online may take about a minute.
   - 🚫  **Usage limits:** It may stop working entirely if the monthly usage limit has been reached.

3. ⚠️ This application **was not** designed or tested for production use. It is an experimental project and **contributions to improve it are welcome and appreciated**!

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

The app uses Python’s library (`re`) to execute regular expression matching for exact keyword detection. The workflow is as follows:

#### 📝 Sentence Segmentation
The app performs sentence segmentation using a regular expression designed to detect sentence boundaries (e.g., periods, question marks) while minimizing false splits (e.g., avoiding splits on abbreviations like "U.S." or "Dr.").

#### 🔍 Case-Insensitive Search with Whole-Word Matching
Each segmented sentence is processed using a regular expression with word boundary markers (\b) to enforce whole-word matching and `re.IGNORECASE` to ensure matching across varying text capitalizations.

#### 📊 Analysis and Output
Upon detecting a keyword, the app logs the occurrence, extracts the corresponding sentence, and increments a frequency counter iteratively for the matched term. Post-processing, the app produces two **.csv** reports:
- Keyword match summary: Enumerates matched terms, their aggregate occurrence counts, and individual frequencies.
- Excerpts: Contains the matched keywords paired with the sentences in which they appear.


### Some Limitations (Others Might Exist!)

- **Scale and Performance**: The app was designed for small-scale, non-production use and handles small documents and files well (e.g., 2–4 pages, files with a few MB in size). Processing large text files or spreadsheets may result in slower performance or failure.
- **Exact Term Matching Only**: The app detects only the exact terms as they appear in the provided list. It does not account for typographical errors or context-dependent meanings.
- **No OCR Support**: The code extracts text only from documents with selectable/searchable text. For scanned images or PDFs without embedded text, an OCR solution would need to be integrated.

  
## References and Links

- U.S. Senate Committee on Commerce, Science & Transportation Report (2024). **DEI: Division. Extremism. Ideology: How the Biden-Harris NSF Politicized Science**. Available at https://www.commerce.senate.gov/services/files/4BD2D522-2092-4246-91A5-58EEF99750BC
  
- [Discover Flask](https://discoverflask.com)
- [Render](https://render.com)

## License
© 2025. This work is openly licensed via CC BY-NC-ND 4.0