from src.parser import extract_resume_text
from src.embedder import calculate_similarity
from src.scorer import skill_match_score
from src.llm import evaluate_candidate

resume = extract_resume_text("data/resume/resume1.pdf")

with open("data/job_description/jd.txt", encoding="utf-8") as f:
    jd = f.read()

similarity = calculate_similarity(jd, resume)

skill_score, matched, missing = skill_match_score(jd, resume)

result = evaluate_candidate(
    jd,
    resume,
    similarity,
    matched,
    missing
)

print(result)