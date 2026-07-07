from src.parser import extract_resume_text
from src.embedder import calculate_similarity

resume_text = extract_resume_text("data/resume/resume1.pdf")

with open("data/job_description/jd.txt", "r", encoding="utf-8") as f:
    jd_text = f.read()

score = calculate_similarity(jd_text, resume_text)

print(f"Similarity Score: {score:.4f}")