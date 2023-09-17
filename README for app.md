# Resume-Matching-with-Job-Descriptions-Using-PDF-CVs by Web Frame Work in Flask

## 1.Install Flask:
  You'll need to have Flask installed. You can install it using pip:
  ### pip install flask

## 2.Create a Flask App:
**Imports:** The script begins by importing the necessary libraries and modules, including Flask, pdfplumber, NumPy, pandas, scikit-learn (for text similarity calculations), NLTK (for text tokenization), and datasets (for loading job descriptions).

**Tokenization and Text Similarity Functions:** The script defines two functions:

**extract_text_from_pdf(pdf_file):** This function uses pdfplumber to extract text from a PDF file and returns the extracted text as a string.
**tokenize_text(text):** This function tokenizes text using NLTK and returns a list of lowercase tokens.

**Flask App Initialization:** The Flask application is initialized with the line app = Flask(__name__).

**Route for Handling File Uploads:** The script defines a single route (/) that handles both GET and POST requests. When a user accesses the root URL of the application, they see an HTML form that allows them to upload a PDF file. When the user submits the form, the uploaded PDF file is processed.

**PDF Processing and Matching:** When a PDF file is uploaded, it is saved temporarily, and its text content is extracted and tokenized. Then, the script calculates the cosine similarity between the uploaded PDF text and a set of predefined job descriptions. The similarity scores are stored in a DataFrame.

**Displaying Results:** The top 5 matches with job descriptions and corresponding companies are displayed on the web page as an HTML table when the form is submitted.

**Running the Application:** The script checks if it is being run directly (if __name__ == "__main__") and, if so, starts the Flask development server with debugging enabled.

## 3.Create HTML Templates:
**HTML Structure:** The file begins with the standard HTML structure, including the <!DOCTYPE> declaration, <html>, <head>, and <body> elements.

**Title:** Inside the <head> section, there is a <title> element that sets the title of the web page to "PDF Matching."

**Form for File Upload:** Within the <body> section, there is an HTML <form> element that allows users to upload a file. This form has the following components:
**<input>:** This input element with type="file" allows users to choose a file from their local device.
**<input>**: Another input element with type="submit" is used to submit the form after selecting a file.

**Conditional Rendering:** The template uses Flask's templating engine to conditionally render content based on the results of file processing. This is achieved with the following Flask template tags:
**{% if top_matches %}:** This block is displayed if the variable top_matches (presumably containing the top matching results) is not empty.
**{% endif %}:** This tag closes the conditional block.

**Displaying Top Matches:** Within the conditional block, there is an <h2> element that displays "Top Matches." Below that, the {{ top_matches | safe }} expression is used to render HTML content stored in the top_matches variable as a table. The | safe filter is used to indicate that the content should be treated as safe HTML and not escaped.

**Dynamic Content:** The template is designed to dynamically display top matching results when a user uploads a PDF file and submits the form.

## 4. Run the Application:
**Check Template Directory**
**Verify HTML File Name**
**Check for Typos and Case Sensitivity**

## 5.Usage:
Users can visit the web page, upload a PDF file, and click the "Upload and Match" button to see the top matching job descriptions and companies based on the cosine similarity.
