# Resume Parser

## Introduction

Resume Parser is a tool designed to extract key information from resumes in PDF and DOCX formats. It offers both a command-line interface for batch processing and a user-friendly web interface built with Streamlit for interactive use.

## Features

- Parse resumes in PDF and DOCX formats
- Extract essential information:
  - Name
  - Email
  - Phone number
  - Education details
  - Skills
  - Job-specific skills (based on provided job title)
- Command-line interface for batch processing
- Interactive web interface using Streamlit
- Customizable skill and education databases

## Directory Structure

```
RESUMEPARSER/
│
├── data/
│   ├── background.jpg
│   ├── education.csv
│   ├── job_specific_skills.csv
│   └── skills.csv
│ 
├── dummy_resumes/
│ 
├── src/
│   ├── utils/
│   │   ├── clean_text.py
│   │   ├── extract_education.py
│   │   ├── extract_mail.py
│   │   ├── extract_name.py
│   │   ├── extract_phone.py
│   │   ├── extract_skills.py
│   │   └── parser.py
│   │
│   ├── __init__.py
│   └── main.py
│
├── app.py
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/ShishirRijal/Resume-Parser.git
   cd resumeparser
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

### Command-line Interface

To use the Resume Parser from the command line:

```
python src/main.py path/to/resume.pdf "Job Title"
```

Replace `path/to/resume.pdf` with the path to your resume file and `"Job Title"` with the desired job title for skill matching.

### Streamlit Web Interface

To run the Streamlit web application:

```
streamlit run app.py
```

This will launch a web interface where you can:
1. Upload a resume file (PDF or DOCX)
2. Enter a job title
3. Click "Extract Information" to view the parsed results

## Customization

You can customize the skill and education databases by modifying the CSV files in the `data/` directory:

- `education.csv`: List of education qualifications
- `skills.csv`: General skills database
- `job_specific_skills.csv`: Job-specific skills for matching


## Dependencies

- Python 3.7+
- Streamlit
- PyPDF2
- python-docx
- pandas
- (other dependencies as listed in requirements.txt)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
