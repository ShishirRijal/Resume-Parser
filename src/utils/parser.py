"""
parser.py

This script provides functions to parse text from PDF and docx files.

"""

import os

from pdfminer.high_level import extract_text
import docx


def parse_pdf(file_path):
    """
    Parses text from a PDF file.

    Args:
        file_path (str): The path to the PDF file.

    Returns:
        str: The extracted text from the PDF file, or None if an error occurs.
    """
    try:
        text = extract_text(file_path)
        return text
    except Exception as e:
        print(f"Error parsing PDF: {e}")
        return None


def parse_docx(file_path):
    """
    Parses text from a docx file.

    Args:
        file_path (str): The path to the docx file.

    Returns:
        str: The extracted text from the docx file, or None if an error occurs.
    """
    try:
        doc = docx.Document(file_path)
        return "\n".join([para.text for para in doc.paragraphs])
    except Exception as e:
        print(f"Error parsing Doc: {e}")
        return None


# Demonstrate usage of the parse_pdf and parse_docx functions.
if __name__ == "__main__":
    project_dir = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../../", "dummy_resumes")
    )
    # dataset_path = os.path.join(project_dir, "data", "education.csv")

    print(parse_pdf(os.path.join(project_dir, "resume2.pdf")))
    print(parse_docx(os.path.join(project_dir, "resume1.docx")))
