import os
import pandas as pd
import re


# Load degrees from CSV
def load_degrees_from_csv(csv_file_path):
    """
    Load degrees from a CSV file.

    Args:
        csv_file_path (str): The path to the CSV file.

    Returns:
        list: A list of degrees.
    """
    df = pd.read_csv(csv_file_path)
    return df["Major"].tolist()


def extract_degrees_from_resume(resume_text, degrees):
    """
    Extract degrees from the resume text.

    Args:
        resume_text (str): The text of the resume.
        degrees (list): A list of majors.

    Returns:
        list: A list of extracted degrees with prefixes.
    """
    # Create a regex pattern to match any of the degrees
    degree_pattern = r"\b(" + "|".join(map(re.escape, degrees)) + r")\b"

    # Search for degrees in the resume text, using re.IGNORECASE for case insensitivity
    matches = re.findall(degree_pattern, resume_text, re.IGNORECASE)

    # Remove duplicates by converting matches to a set and then back to a list
    return list(set(matches))


def extract_education_with_prefixes(resume_text, degrees):
    """
    Extract educational qualifications from the resume text,
    including degree prefixes and words in between.

    Args:
        resume_text (str): The text of the resume.
        degrees (list): A list of majors.

    Returns:
        list: A list of extracted educational qualifications.
    """
    # Extract degrees without prefixes
    extracted_degrees = extract_degrees_from_resume(resume_text, degrees)

    # Define prefixes to check
    prefixes = ["Bachelor", "Master", "Ph.D.", "Doctor of", "Associate Degree"]

    # List to hold results
    education_qualifications = []

    # Check for prefixes and combine with the extracted degrees
    for degree in extracted_degrees:
        for prefix in prefixes:
            # Create a pattern that allows for any text between prefix and degree
            prefix_pattern = rf"\b({prefix})\s+(.*?)\s*({re.escape(degree)})\b"
            match = re.search(prefix_pattern, resume_text, re.IGNORECASE)
            if match:
                # Include the prefix, the words in between, and the degree in the output
                education_qualifications.append(
                    f"{match.group(1)} {match.group(2).strip()} {match.group(3)}"
                )

    return list(set(education_qualifications))


# Example usage
if __name__ == "__main__":
    project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    csv_file_path = os.path.join(project_dir, "data", "education.csv")
    resume_text = """
    John Doe
    Education: 
    Bachelor of Science in COMPUTER SCIENCE
    Master of Arts in History
    Ph.D. in Physics
    High School Diploma
    """

    degrees_list = load_degrees_from_csv(csv_file_path)

    print(extract_education_with_prefixes(resume_text, degrees_list))
