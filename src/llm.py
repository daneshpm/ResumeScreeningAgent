import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def evaluate_candidate(jd_text, resume_text, similarity, matched, missing):

    prompt = f"""
You are an experienced HR recruiter.

Evaluate this candidate for the given job.

Job Description:
{jd_text}

Resume:
{resume_text}

Similarity Score:
{similarity:.2f}

Matched Skills:
{matched}

Missing Skills:
{missing}

Return ONLY in this format:

Strengths:
- ...

Weaknesses:
- ...

Recommendation:
...
"""

    response = model.generate_content(prompt)

    return response.text