# 🚀 Resume Parser

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io/)
[![pdfminer](https://img.shields.io/badge/pdfminer-red?style=for-the-badge&logo=adobe-acrobat-reader&logoColor=white)](https://github.com/pdfminer/pdfminer.six)
[![python-docx](https://img.shields.io/badge/python--docx-blue?style=for-the-badge&logo=microsoft-word&logoColor=white)](https://python-docx.readthedocs.io/)
[![pandas](https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)





## 🌟 Introduction

Resume Parser is a NLP tool designed to extract key information from resumes in PDF and DOCX formats. It offers both a command-line interface for batch processing and a user-friendly web interface built with Streamlit for interactive use.

## ✨ Features

- 📄 Parse resumes in PDF and DOCX formats
- 🔍 Extract essential information:
  - 👤 Name
  - 📧 Email
  - 📱 Phone number
  - 🎓 Education details
  - 🛠️ Skills
  - 💼 Job-specific skills (based on provided job title)
- 💻 Command-line interface for batch processing
- 🌐 Interactive web interface using Streamlit
- 🔧 Customizable skill and education databases

## 📁 Directory Structure

```
RESUME-PARSER/
│
├── 📂 data/
│   ├── 🖼️ background.jpg
│   ├── 📚 education.csv
│   ├── 💼 job_specific_skills.csv
│   └── 🛠️ skills.csv
│ 
├── 📂 dummy_resumes/
│ 
├── 📂 src/
│   ├── 📂 utils/
│   │   ├── 🧹 clean_text.py
│   │   ├── 🎓 extract_education.py
│   │   ├── 📧 extract_mail.py
│   │   ├── 👤 extract_name.py
│   │   ├── 📱 extract_phone.py
│   │   ├── 🛠️ extract_skills.py
│   │   └── 📄 parser.py
│   │
│   ├── 📜 __init__.py
│   └── 🚀 main.py
│
├── 🌐 app.py
├── 📋 requirements.txt
└── 📖 README.md
```

## 🛠️ Installation

1. Clone the repository:
   ```
   git clone https://github.com/ShishirRijal/Resume-Parser.git
   cd Resume-Parser
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

## 🚀 Usage

### 💻 Command-line Interface

To use the Resume Parser from the command line:

```
python src/main.py path/to/resume.pdf "Job Title"
```

Replace `path/to/resume.pdf` with the path to your resume file and `"Job Title"` with the desired job title for skill matching.

### 🌐 Streamlit Web Interface

To run the Streamlit web application:

```
streamlit run app.py
```

This will launch a web interface where you can:
1. 📤 Upload a resume file (PDF or DOCX)
2. 💼 Enter a job title
3. 🔍 Click "Extract Information" to view the parsed results

## 🔧 Customization

You can customize the skill and education databases by modifying the CSV files in the `data/` directory:

- 📚 `education.csv`: List of education qualifications
- 🛠️ `skills.csv`: General skills database
- 💼 `job_specific_skills.csv`: Job-specific skills for matching

## 🔧 Dependencies

- [![Python](https://img.shields.io/badge/Python-3.7%2B-blue?style=flat-square&logo=python)](https://www.python.org/)
- [![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=Streamlit&logoColor=white)](https://streamlit.io/)
- [![pandas](https://img.shields.io/badge/pandas-150458?style=flat-square&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
- [![pdfminer](https://img.shields.io/badge/pdfminer-red?style=flat-square&logo=adobe-acrobat-reader&logoColor=white)](https://github.com/pdfminer/pdfminer.six)
- [![python-docx](https://img.shields.io/badge/python--docx-blue?style=flat-square&logo=microsoft-word&logoColor=white)](https://python-docx.readthedocs.io/)


## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📸 Snaps

<img width="1466" alt="Screenshot 2024-10-16 at 3 42 24 PM" src="https://github.com/user-attachments/assets/8cdd2d30-a423-424b-bc61-fee1378cbb88">
<img width="1463" alt="Screenshot 2024-10-16 at 3 42 44 PM" src="https://github.com/user-attachments/assets/a9308717-70be-471f-aa4f-4ddba82d015a">
<img width="1469" alt="Screenshot 2024-10-16 at 3 43 08 PM" src="https://github.com/user-attachments/assets/13e75a03-3ab2-43f8-8304-b60fe9b3d452">
<img width="1464" alt="Screenshot 2024-10-16 at 3 43 23 PM" src="https://github.com/user-attachments/assets/7827a2b8-9ae5-4ac6-bae0-c457efddb21b">

## 🌟 Awesome Resources

- [![Awesome](https://awesome.re/badge.svg)](https://awesome.re) 
- [Awesome Python](https://github.com/vinta/awesome-python)
- [Awesome Streamlit](https://github.com/MarcSkovMadsen/awesome-streamlit)
- [Awesome PDF](https://github.com/py-pdf/awesome-pdf)
- [Awesome NLP](https://github.com/keon/awesome-nlp)

## 🚀 Future Enhancements

- 🧠 Implement machine learning for improved accuracy
- 🌐 Add support for more file formats
- 🔗 Integrate with job posting APIs for better skill matching
- 📊 Implement data visualization for parsed results

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check [issues page](https://github.com/ShishirRijal/Resume-Parser/issues).

## 🌟 Show your support

Give a ⭐️ if this project helped you!

## 📞 Contact

Shishir Rijal - [@ShishirRijal](https://github.com/ShishirRijal)

Project Link: [https://github.com/ShishirRijal/Resume-Parser](https://github.com/ShishirRijal/Resume-Parser)

---

Made with 💖 and ☕️ by Shishir Rijal
