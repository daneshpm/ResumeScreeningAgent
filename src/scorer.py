import re

SKILLS = [
    "python",
    "java",
    "spring boot",
    "sql",
    "mysql",
    "postgresql",
    "mongodb",
    "git",
    "docker",
    "aws",
    "linux",
    "jenkins",
    "kubernetes",
    "ci/cd",
    "rest api",
    "restful api",
    "hibernate",
    "jpa",
    "react",
    "javascript",
    "html",
    "css",
    "machine learning",
    "deep learning",
    "tensorflow",
    "pytorch",
    "communication",
    "problem solving",
    "data structures"
]


def extract_skills(text):
    text = text.lower()

    found = []

    for skill in SKILLS:
        if skill in text:
            found.append(skill)

    return list(set(found))


def skill_match_score(jd_text, resume_text):

    jd_skills = extract_skills(jd_text)

    resume_skills = extract_skills(resume_text)

    if len(jd_skills) == 0:
        return 0, [], []

    matched = list(set(jd_skills) & set(resume_skills))

    missing = list(set(jd_skills) - set(resume_skills))

    score = len(matched) / len(jd_skills)

    return score, matched, missing