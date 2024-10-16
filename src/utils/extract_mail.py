"""
extract_email.py

This script extracts mail address from a resume.

"""

import re
import spacy


def extract_email_from_resume(resume_text):
    """
    Extract the applicant's email address from the resume text.

    Args:
        resume_text (str): The text of the resume.

    Returns:
        str: The extracted email address, or an empty string if not found.
    """
    email_regex = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
    match = re.search(email_regex, resume_text)
    if match:
        return match.group()


# * Alternative Approach [Using Spacy]
# While regular expressions are often sufficient for simple email extraction,
# spaCy offers an alternative approach that might be useful in more complex scenarios.
# However, spaCy can introduce performance overhead
# compared to a regular expression for this specific task.


def extract_email_using_spacy(resume_text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(resume_text)
    for token in doc:
        if token.like_email:
            return token.text
    return ""


# Example usage
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

    email = extract_email_from_resume(resume_text)
    if email:
        print(f"Extracted email: {email}")
    else:
        print("No email address found.")
