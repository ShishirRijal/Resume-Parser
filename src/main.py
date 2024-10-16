import os

from utils.parser import parse_pdf, parse_docx
from utils.clean_text import clean_text
from utils.extract_education import extract_education
from utils.extract_mail import extract_email
from utils.extract_name import extract_name
from utils.extract_phone import extract_phone_number
from utils.extract_skills import (
    extract_skills_from_resume,
    match_skills_with_job,
)


project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
data_dir_path = os.path.join(project_dir, "data")
print(data_dir_path)


def parse_resume(file_path, job_title):
    # Let's parse the resume first...
    if file_path.endswith(".pdf"):
        raw_text = parse_pdf(file_path)
    elif file_path.endswith(".docx"):
        raw_text = parse_docx(file_path)
    else:
        print("Unsupported file format!")
        return

    # Preprocess the text
    clean_resume = clean_text(raw_text)

    # Extract the necessary information
    name = extract_name(clean_resume)
    email = extract_email(clean_resume)
    phone_number = extract_phone_number(clean_resume)
    education = extract_education(clean_resume)
    skills = extract_skills_from_resume(clean_resume)
    job_specific_skills = match_skills_with_job(job_title, clean_resume)

    # Print the extracted information in a readable format
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Phone Number: {phone_number}")
    print(f"Education:")
    for degree in education:
        print(f"\t- {degree}")

    print(f"Applicant's Skills:")
    if not skills:
        print("No skills found")
    else:
        for skill in skills:
            print(f"\t- {skill}")

    print(f"Applicant's skills for {job_title}:")
    if not job_specific_skills:
        print(f"No skills found for {job_title}")
    else:
        for skill in job_specific_skills:
            print(f"\t- {skill}")


if __name__ == "__main__":
    file_path = input("Enter the file path [Leave empty for default]: ")
    if file_path == "":
        file_path = os.path.join(project_dir, "dummy_resumes", "resume2.pdf")
    parse_resume(file_path)
