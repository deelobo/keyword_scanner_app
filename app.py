import os
import re
import pandas as pd
import fitz  # PyMuPDF for PDFs
import docx  # For Word documents
from flask import Flask, request, render_template, send_file

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
RESULTS_FOLDER = "results"
KEYWORDS_FILE = "dei_terms.txt"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULTS_FOLDER, exist_ok=True)


# Function to extract text from different file types
def extract_text_from_file(file_path):
    text = ""
    try:
        if file_path.lower().endswith(".txt"):
            with open(file_path, "r", encoding="utf-8") as file:
                text = file.read()
        elif file_path.lower().endswith(".pdf"):
            text = extract_text_from_pdf(file_path)
        elif file_path.lower().endswith(".docx"):
            text = extract_text_from_word(file_path)
        elif file_path.lower().endswith((".xls", ".xlsx")):
            text = extract_text_from_excel(file_path)
        elif file_path.lower().endswith((".csv")):
            text = extract_text_from_csv(file_path)
        else:
            print(f"Unsupported file type: {file_path}")
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    return text


# Extract text from PDFs
def extract_text_from_pdf(file_path):
    text = ""
    try:
        with fitz.open(file_path) as doc:
            for page in doc:
                text += page.get_text()
    except Exception as e:
        print(f"Error reading PDF {file_path}: {e}")
    return text


# Extract text from Word documents
def extract_text_from_word(file_path):
    text = ""
    try:
        doc = docx.Document(file_path)
        for paragraph in doc.paragraphs:
            text += paragraph.text + "\n"
    except Exception as e:
        print(f"Error reading Word document {file_path}: {e}")
    return text


# Extract text from Excel files
def extract_text_from_excel(file_path):
    text = ""
    try:
        df = pd.read_excel(file_path, engine="openpyxl")
        for column in df.columns:
            text += " ".join(df[column].astype(str).tolist()) + " "
    except Exception as e:
        print(f"Error reading Excel file {file_path}: {e}")
    return text


# Extract text from CSV files
def extract_text_from_csv(file_path):
    text = ""
    try:
        df = pd.read_csv(file_path)
        for column in df.columns:
            text += " ".join(df[column].astype(str).tolist()) + " "
    except Exception as e:
        print(f"Error reading CSV file {file_path}: {e}")
    return text


# Load keywords from file
def load_keywords():
    try:
        with open(KEYWORDS_FILE, "r", encoding="utf-8") as file:
            return [line.strip() for line in file if line.strip()]
    except Exception as e:
        print(f"Error reading keyword file: {e}")
        return []


# Extract sentences with keywords
def extract_sentences_with_keywords(text, keywords):
    sentences = re.split(r"(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s", text)
    results = []
    for sentence in sentences:
        for keyword in keywords:
            if re.search(rf"\b{re.escape(keyword)}\b", sentence, re.IGNORECASE):
                results.append({"Matched_Term": keyword, "Excerpt": sentence.strip()})
    return results


# Keyword frequency count
def keyword_search(text, keywords):
    matched_terms = {}
    for keyword in keywords:
        matches = re.findall(rf"\b{re.escape(keyword)}\b", text.lower())
        if matches:
            matched_terms[keyword] = len(matches)
    return matched_terms


# Process uploaded files
def process_files(files):
    keywords = load_keywords()
    summary_results = []
    excerpt_results = []

    for file in files:
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)

        text = extract_text_from_file(file_path)
        if text:
            matched_terms = keyword_search(text, keywords)
            summary_results.append(
                {
                    "File_Name": file.filename,
                    "Matched_Terms": (
                        ", ".join(matched_terms.keys()) if matched_terms else "None"
                    ),
                    "Total_Term_Count": len(matched_terms),
                    "Term_Frequency": matched_terms,
                }
            )

            excerpts = extract_sentences_with_keywords(text, keywords)
            for excerpt in excerpts:
                excerpt["File_Name"] = file.filename
                excerpt_results.append(excerpt)

    summary_df = pd.DataFrame(summary_results)
    excerpt_df = pd.DataFrame(excerpt_results)

    summary_file_path = os.path.join(RESULTS_FOLDER, "summary_results.csv")
    excerpt_file_path = os.path.join(RESULTS_FOLDER, "excerpt_results.csv")

    summary_df.to_csv(summary_file_path, index=False)
    excerpt_df.to_csv(excerpt_file_path, index=False)

    return summary_file_path, excerpt_file_path


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "files[]" not in request.files:
            return "No file uploaded", 400

        files = request.files.getlist("files[]")
        summary_file, excerpt_file = process_files(files)

        return render_template(
            "index.html", summary_file=summary_file, excerpt_file=excerpt_file
        )

    return render_template("index.html")


@app.route("/download/<filename>")
def download_file(filename):
    return send_file(os.path.join(RESULTS_FOLDER, filename), as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
