# Resume-Matching-with-Job-Descriptions-Using-PDF-CVs
## Build a PDF extractor to pull relevant details from CVs in PDF format, and match them against the job descriptions from the Hugging Face dataset.
### 1. PDF Data Extraction
**Objective:** Extract details from CVs in PDF format.

**Dataset:** Kaggle Resume Dataset

**Instructions:**
Download the Kaggle "resume dataset".
Build a PDF extractor using Python, leveraging libraries such as PyPDF2 or
PDFMiner.

### 2. Job Description Data Understanding

**Objective: **Fetch and comprehend job descriptions from the Hugging Face dataset.

**Dataset:** Job Descriptions from Hugging Face

**Instructions:**
Use the Hugging Face datasets library to fetch the job descriptions. For this task,
consider extracting 10-15 job descriptions.

### 3. Candidate-Job Matching
Objective: Match extracted CV details against the fetched job descriptions.

**Instructions:**
Tokenize and preprocess both the job descriptions and the extracted CV details from
the PDFs.
For each job description, calculate the cosine similarity between its embedding and
the embeddings of the CVs.
Rank CVs based on this similarity for each job description.
List the top 5 CVs for each job description based on the highest similarity scores.
