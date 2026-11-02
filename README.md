
# AI Resume Analyzer & Job Match Assistant

An AI-powered web application that analyzes resumes against job descriptions and provides personalized feedback to help candidates improve their job suitability.

Built using **Python, Streamlit, LangChain, and Groq LLM**.

## Features

- **Resume Upload:** Upload resumes in PDF, DOCX, or TXT format.
- **Text Extraction:** Extract resume content using LangChain document loaders.
- **AI-Powered Analysis:** Analyze resumes against job descriptions using Groq LLM.
- **Candidate Summary:** Generate a brief professional profile.
- **Skills Identification:** Identify technical skills mentioned in the resume.
- **Skill Matching:** Highlight matched and missing skills based on the job description.
- **Resume Evaluation:** Identify strengths and weaknesses.
- **ATS Optimization:** Provide suggestions to improve resume readability and ATS compatibility.
- **Improvement Recommendations:** Suggest practical ways to improve job suitability.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend development |
| Streamlit | User interface |
| LangChain | Document processing and LLM integration |
| Groq | Large Language Model inference |
| PyPDF | PDF text extraction |
| Docx2txt | DOCX text extraction |

## Project Structure

```text
ai_resume_reviewer/
│
├── AI_resume_reviewer.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/umapravallika/ai_resume_reviewer.git
```

### 2. Navigate to the project directory

```bash
cd ai_resume_reviewer
```

### 3. Create a virtual environment (optional)

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure the Groq API key

Create a folder named `.streamlit` in the project directory.

Inside it, create `secrets.toml`:

```toml
GROQ_API_KEY = "your_groq_api_key"
```

Get an API key from [Groq Console](https://console.groq.com/).

**Important:** Never upload your API key or `secrets.toml` file to GitHub.

### 6. Run the application

```bash
streamlit run AI_resume_reviewer.py
```

The application will open in your browser.

## How to Use

1. Open the application.
2. Upload your resume in PDF, DOCX, or TXT format.
3. Paste the target job description.
4. Click **Analyze My Resume**.
5. Review the AI-generated analysis and improvement suggestions.

## Deployment

This application is deployed using **Streamlit Community Cloud**.

**Live Application:** [AI Resume Analyzer & Job Match Assistant](https://umapravallika-ai-resume-reviewer-ai-resume-reviewer-mprdo6.streamlit.app/)

## Future Enhancements

- Resume match percentage based on actual skill matching.
- Downloadable resume analysis report in PDF format.
- Personalized interview questions based on the job description.
- Resume improvement suggestions.
- Enhanced dashboard with interactive visualizations.
- Support for additional document formats.

## Author

**Uma Pravallika Chikkam**

B.Tech – Computer Science and Engineering

GitHub: [umapravallika](https://github.com/umapravallika)

---

If you find this project useful, feel free to explore the repository and share your feedback!
