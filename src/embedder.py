from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load model only once
model = SentenceTransformer("all-MiniLM-L6-v2")


def get_embedding(text):
    return model.encode(text)


def calculate_similarity(jd_text, resume_text):
    jd_embedding = get_embedding(jd_text)
    resume_embedding = get_embedding(resume_text)

    score = cosine_similarity(
        [jd_embedding],
        [resume_embedding]
    )[0][0]

    return float(score)