from flask import Flask, request, render_template
import os
from datasets import load_dataset
import pdfplumber
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from nltk.tokenize import word_tokenize

# Initialize Flask app
app = Flask(__name__)

# Download necessary NLTK resources
nltk.download('punkt')

# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_file):
    with pdfplumber.open(pdf_file) as pdf:
        text = []
        for page in pdf.pages:
            text.append(page.extract_text())
        return ''.join(text).replace("\n", "")

# Tokenize text using NLTK
def tokenize_text(text):
    text = text.lower()
    return word_tokenize(text)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Handle file upload
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            # Save the uploaded file temporarily
            pdf_path = "temp.pdf"
            uploaded_file.save(pdf_path)

            # Process the uploaded PDF
            CV_Clear = extract_text_from_pdf(pdf_path)
            CV_Clear_tokens = tokenize_text(CV_Clear)

            # Load job descriptions dataset (you can adapt this to your dataset)
            dataset = load_dataset("jacob-hugging-face/job-descriptions")
            job_descriptions = dataset["train"]["model_response"][:15]
            company_names = dataset["train"]["company_name"][:15]

            # Initialize a dictionary to store match percentages for each company
            company_match_percentages = {company_name: [] for company_name in company_names}

            # Calculate cosine similarity with each job description
            for company_name, job_description in zip(company_names, job_descriptions):
                job_description_tokens = tokenize_text(job_description)
                Match_Test = [' '.join(CV_Clear_tokens), ' '.join(job_description_tokens)]
                cv = CountVectorizer()
                count_matrix = cv.fit_transform(Match_Test)
                similarity = cosine_similarity(count_matrix)[0][1] * 100
                company_match_percentages[company_name].append(similarity)

            # Initialize a dictionary to store company match percentages and file names
            data = {'Pdf Number': [pdf_path]}

            # Add match percentages for each company
            for company_name in company_names:
                data[company_name] = company_match_percentages[company_name]

            # Create a DataFrame to store the results
            result_df = pd.DataFrame(data)

            # Add a new column 'Max Similarity' to store the maximum similarity for each row (PDF)
            result_df['Max Similarity'] = result_df[company_names].max(axis=1)

            # Sort the DataFrame by the maximum similarity in descending order
            result_df = result_df.sort_values(by='Max Similarity', ascending=False)

            # Display the top 5 rows
            top_matches = result_df.head(5).to_html(classes='table table-striped')

            # Delete the temporary PDF file
            os.remove(pdf_path)

            return render_template('index.html', top_matches=top_matches)

    return render_template('index.html', top_matches=None)

if __name__ == "__main__":
    app.run(debug=True)
