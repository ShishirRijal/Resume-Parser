import streamlit as st
import os
from PIL import Image
import base64

from src.utils.parser import parse_pdf, parse_docx
from src.utils.clean_text import clean_text
from src.utils.extract_education import extract_education
from src.utils.extract_mail import extract_email
from src.utils.extract_name import extract_name
from src.utils.extract_phone import extract_phone_number
from src.utils.extract_skills import extract_skills_from_resume, match_skills_with_job

# Get the current working directory
project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__)))
data_dir_path = os.path.join(project_dir, "data")


# Function to set background image
def set_bg_hack():
    image_path = os.path.join(data_dir_path, "background.jpg")
    main_bg_ext = "png"
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(image_path, "rb").read()).decode()});
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )


# Function to create a custom card
def custom_card(title, content):
    st.markdown(
        f"""
    <div style="background-color: rgba(255, 255, 255, 0.1); padding: 20px; border-radius: 10px; backdrop-filter: blur(10px);">
        <h3 style="color: #4AF626;">{title}</h3>
        <p style="color: #FFFFFF;">{content}</p>
    </div>
    """,
        unsafe_allow_html=True,
    )


# Streamlit app
def main():
    # Set background image
    set_bg_hack()

    # Custom CSS
    st.markdown(
        """
    <style>
    .big-font {
        font-size:50px !important;
        color: #4AF626;
        font-weight: bold;
    }
    
    .stButton>button {
        color: #4AF626;
        background-color: transparent;
        border: 2px solid #4AF626;
    }
    
    .stButton>button:hover {
        background-color: rgba(74, 246, 38, 0.2);
    }
    </style>
    """,
        unsafe_allow_html=True,
    )

    st.markdown(
        '<p class="big-font">Futuristic Resume Parser</p>', unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        # Job title field with a custom label and placeholder
        job_title = st.text_input("Job Title", placeholder="e.g., Data Scientist")

    with col2:
        # File uploader with a custom label
        uploaded_file = st.file_uploader("Upload Resume", type=["pdf", "docx"])

    if uploaded_file is not None:
        # Parse the uploaded file
        file_bytes = uploaded_file.read()
        file_path = os.path.join(data_dir_path, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(file_bytes)

        # Extract Information button
        if st.button("Extract Information"):
            with st.spinner("Parsing resume..."):
                # Parse the resume
                resume_text = parse_resume(file_path, job_title)

            # Display extracted information
            st.markdown("### Extracted Information")

            col1, col2 = st.columns(2)
            with col1:
                custom_card("Name", resume_text["name"])
                st.markdown("<br>", unsafe_allow_html=True)
                custom_card("Email", resume_text["email"])
                st.markdown("<br>", unsafe_allow_html=True)
                custom_card("Phone Number", resume_text["phone_number"])

            with col2:
                custom_card("Education", "<br>".join(resume_text["education"]))
                st.markdown("<br>", unsafe_allow_html=True)
                custom_card("Skills", "<br>".join(resume_text["skills"]))
                st.markdown("<br>", unsafe_allow_html=True)
                custom_card(
                    f"Job-Specific Skills (for {job_title})",
                    "<br>".join(resume_text["job_specific_skills"]),
                )


# Define the `parse_resume` function
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

    # Return a dictionary containing extracted information
    return {
        "name": name,
        "email": email,
        "phone_number": phone_number,
        "education": education,
        "skills": skills,
        "job_specific_skills": job_specific_skills,
    }


if __name__ == "__main__":
    main()
