"""
parser.py

This script provides functions to parse text from PDF and docx files.

"""

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
        print(f"Error parsing PDF: {e}")
        return None


# Demonstrate usage of the parse_pdf and parse_docx functions.
if __name__ == "__main__":
    print(
        parse_pdf(
            "/Users/shishirrijal/Desktop/NLP/ResumeParser/dummy_resumes/resume2.pdf"
        )
    )
    print(
        parse_docx(
            "/Users/shishirrijal/Desktop/NLP/ResumeParser/dummy_resumes/resume1.docx"
        )
    )
