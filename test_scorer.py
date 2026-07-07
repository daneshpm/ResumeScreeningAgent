from src.parser import extract_resume_text
from src.scorer import skill_match_score

resume = extract_resume_text("data/resume/resume1.pdf")

with open("data/job_description/jd.txt", encoding="utf-8") as f:
    jd = f.read()

score, matched, missing = skill_match_score(jd, resume)

print("Skill Score:", score)

print("\nMatched Skills")
print(matched)

print("\nMissing Skills")
print(missing)