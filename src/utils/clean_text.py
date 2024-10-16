"""
clean_text.py

This script provides a function to clean text by removing punctuation, extra spaces,
converting to lowercase, and removing stopwords.

"""

import re
import nltk
from nltk.corpus import stopwords

nltk.download("stopwords")
stop_words = set(stopwords.words("english"))


def clean_text(text):
    """
    Cleans text by removing punctuation, extra spaces, converting to lowercase,
    and removing stopwords.

    Args:
        text (str): The text to be cleaned.

    Returns:
        str: The cleaned text.
    """
    text = re.sub(r"\n+", "\n", text)  # Remove extra newlines
    # removing the punctuation was causing issues with phone numbers and emails
    # text = re.sub(r"[^\w\s]", " ", text)  # Remove punctuation
    text = re.sub(r"\s+", " ", text)  # Remove extra spaces
    text = text.lower()  # Convert to lowercase

    # Tokenize and remove stopwords
    tokens = text.split()
    tokens = [word for word in tokens if word not in stop_words]

    return " ".join(tokens)


# Demonstrate usage of the clean_text function.
if __name__ == "__main__":
    resume_text = """
JACQUELINE THOMPSON

123 Anywhere St., Any City • 123-456-7890 • hello@reallygreatsite.com
www.reallygreatsite.com

SUMMARY

Results-oriented Engineering Executive with a proven track record of optimizing project outcomes.
Skilled in strategic project management and team leadership. Seeking a challenging executive role
to leverage technical expertise and drive engineering excellence.

WORK EXPERIENCE

Engineering Executive , Borcelle Technologies

Jan 2023 - Present

Implemented cost-effective solutions, resulting in a 20% reduction in project expenses.
Streamlined project workflows, enhancing overall efficiency by 25%.
Led a team in successfully delivering a complex engineering project on time and within
allocated budget.

Project Engineer, Salford & Co

Mar 2021 - Dec 2022
...
Awards/Activities: Received the "Engineering Excellence" Award for outstanding
contributions to project innovation, Borcelle Technologies
    """
    print(clean_text(resume_text))
