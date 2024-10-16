"""
extract_phone.py

This script extracts phone number of applicant from a resume.

"""

import re


def extract_phone_number_from_resume(resume_text):
    """
    Extract the applicant's phone number from the resume text.

    Args:
        resume_text (str): The text of the resume.

    Returns:
        str: The extracted phone number, or "No phone number found" if not found.
    """
    # Regex pattern for phone numbers
    phone_regex = r"(\+?\d{1,3}[-.\s]?)?(\(?\d{3}\)?[-.\s]?)?\d{3}[-.\s]?\d{4}"

    match = re.search(phone_regex, resume_text)
    if match:
        return match.group()

    return "No phone number found"


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

    phone_number = extract_phone_number_from_resume(resume_text)
    print(f"Extracted Phone Number: {phone_number}")
