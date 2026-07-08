# AI Resume Screening & Candidate Ranking System

An AI-powered Applicant Tracking System (ATS) that automatically ranks resumes against a job description using semantic similarity, skill matching, and Google's Gemini AI for recruiter-style candidate evaluation.

---

## Features

- Parse resumes (PDF, DOCX, TXT)
- Semantic similarity using Sentence Transformers
- Skill extraction and matching
- AI-powered recruiter evaluation using Gemini
- Candidate ranking based on weighted score
- Interactive Streamlit dashboard
- Export results to CSV and JSON

---

## Tech Stack

- Python
- Streamlit
- Sentence Transformers
- PyTorch
- Google Gemini API
- Scikit-learn
- PyMuPDF
- python-docx
- Pandas

---

##  Project Structure

```
ResumeScreeningAgent/
│
├── app.py
├── requirements.txt
├── README.md
├── .env.example
├── architecture.png
│
├── src/
│   ├── parser.py
│   ├── embedder.py
│   ├── scorer.py
│   ├── llm.py
│   └── exporter.py
│
├── data/
│   ├── resumes/
│   └── job_description/
│
├── output/
│
└── screenshots/
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/daneshpm/ResumeScreeningAgent.git

cd ResumeScreeningAgent
```

Create a virtual environment

```bash
python -m venv venv
```

Activate it

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```text
GEMINI_API_KEY=YOUR_API_KEY
```

Run the application

```bash
streamlit run app.py
```

---

##  How It Works

1. Upload a Job Description
2. Upload one or more resumes
3. Extract text from each resume
4. Generate semantic embeddings
5. Calculate similarity score
6. Extract and compare skills
7. Generate AI recruiter evaluation using Gemini
8. Rank candidates
9. Export results as CSV or JSON

---

## Scoring Logic

The final candidate score is calculated using:

```
Final Score =
70% Semantic Similarity +
30% Skill Match
```

Semantic similarity is calculated using Sentence Transformers.

Skill matching compares extracted resume skills with the required job description skills.

---

##  Architecture

<img width="283" height="995" alt="ResumePaser" src="https://github.com/user-attachments/assets/c4b4a516-fbe0-485f-98b6-1460472d7ce2" />



---

## 📸 Screenshots
<img width="1908" height="930" alt="Screenshot 2026-07-08 000605" src="https://github.com/user-attachments/assets/e0340e1e-7f6c-4f84-9388-392fd173d3b7" />
<img width="1905" height="812" alt="Screenshot 2026-07-08 002855" src="https://github.com/user-attachments/assets/edbc1d42-daad-4ba9-9c30-d9edd8cb9cf1" />
<img width="1910" height="8362" alt="screencapture-localhost-8501-2026-07-08-00_32_00" src="https://github.com/user-attachments/assets/1ba40641-e3f2-4c96-83a1-2bd83062d47e" />



---

##  Design Decisions & Trade-offs

- Sentence Transformers are used for deterministic semantic matching because they are fast, consistent, and cost-effective.
- Gemini is used only for qualitative recruiter-style reasoning instead of numerical scoring.
- A lightweight skill dictionary is used for explainability and simplicity within the project timeline.
- The application focuses on an end-to-end working pipeline rather than advanced ATS features such as OCR or authentication.

---

## Future Improvements

- Experience extraction
- Resume summarization
- Automatic skill extraction using LLMs
- Recruiter authentication
- Cloud deployment
- Interview question generation

---

##  Author

**Danesh P M**

GitHub: https://github.com/daneshpm
