from src.parser import extract_resume_text

resume = "data/resume/resume1.pdf"

text = extract_resume_text(resume)

print(text[:1000])