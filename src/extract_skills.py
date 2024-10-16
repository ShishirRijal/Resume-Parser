"""
skills_extractor.py

This script extracts skills from a resume and matches them with job-specific skills.

"""

import pandas as pd
import os


# Get the current working directory
project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Construct the file paths
skills_file_path = os.path.join(project_dir, "data", "skills.csv")
job_specific_skills_file_path = os.path.join(
    project_dir, "data", "job_specific_skills.csv"
)

# Load the CSV files
job_specific_skills_df = pd.read_csv(job_specific_skills_file_path)
skills_df = pd.read_csv(skills_file_path)


def extract_skills_from_resume(resume_text):
    """
    Extracts skills from a resume text.

    Args:
        resume_text (str): The resume text.

    Returns:
        list[str]: A list of extracted skills.
    """
    extracted_skills = []

    for skill in skills_df["Text"]:
        if skill.lower() in resume_text.lower():
            extracted_skills.append(skill)
    # remove duplicate skills if any
    extracted_skills = list(set(extracted_skills))
    return extracted_skills


def match_skills_with_job(job_role, resume_text):
    """
    Matches skills from a resume with job-specific skills.

    Args:
        job_role (str): The job role.
        resume_text (str): The resume text.

    Returns:
        list[str]: A list of matched skills.
    """
    # Extract skills from the resume
    extracted_skills = extract_skills_from_resume(resume_text)

    # Get skills required for the job role
    required_skills = get_skills_by_job_role(job_role)

    # Find matched skills
    matched_skills = set(extracted_skills).intersection(set(required_skills))

    return list(matched_skills)


def get_skills_by_job_role(job_role):
    """
    Gets skills required for a given job role.

    Args:
        job_role (str): The job role.

    Returns:
        list[str]: A list of required skills.
    """
    job_role = job_role.lower()

    # Find the row that matches the job role
    matched_row = job_specific_skills_df[
        job_specific_skills_df.iloc[:, 0].str.lower() == job_role
    ]

    if not matched_row.empty:
        # Extract skills from the matched row
        skills = matched_row.iloc[0, 1:].dropna().tolist()
        return [skill for skill in skills if isinstance(skill, str)]

    return []


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
    job = "project manager"
    print("Skills extracted from resume: ", extract_skills_from_resume(resume_text))
    print(f"Skills requried for the job of '{job}' : ", get_skills_by_job_role(job))
    print(
        f"Applicant's skills for the job of '{job}': ",
        match_skills_with_job(job, resume_text),
    )
