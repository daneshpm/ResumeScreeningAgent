import streamlit as st
import tempfile
import os
import pandas as pd

from src.parser import extract_resume_text
from src.embedder import calculate_similarity
from src.scorer import skill_match_score
from src.llm import evaluate_candidate
from src.exporter import export_csv, export_json

st.set_page_config(
    page_title="AI Resume Screening & Candidate Ranking System",
    page_icon="**",
    layout="wide"
)

# ---------------- Sidebar ---------------- #

with st.sidebar:
    st.title("AI Resume Agent")

    st.markdown("""
### Features

- Resume Parsing
- Semantic Similarity
- Skill Matching
- Gemini AI Evaluation
- Candidate Ranking
- CSV Export
- JSON Export
""")

# ---------------- Header ---------------- #

st.title("AI Resume Screening & Candidate Ranking System")
st.caption("Powered by Sentence Transformers + Gemini AI")

st.write("Upload a Job Description and one or more resumes.")

# ---------------- Uploads ---------------- #

jd_file = st.file_uploader(
    "Upload Job Description",
    type=["txt"]
)

resume_files = st.file_uploader(
    "Upload Resumes",
    type=["pdf", "docx", "txt"],
    accept_multiple_files=True
)

# ---------------- Analyze ---------------- #

if st.button("Analyze Candidates"):

    if jd_file is None:
        st.warning("Please upload a Job Description.")
        st.stop()

    if not resume_files:
        st.warning("Please upload at least one resume.")
        st.stop()

    jd_text = jd_file.read().decode("utf-8")

    results = []

    with st.spinner("Analyzing resumes..."):

        for uploaded_resume in resume_files:

            with tempfile.NamedTemporaryFile(
                delete=False,
                suffix=os.path.splitext(uploaded_resume.name)[1]
            ) as temp_file:

                temp_file.write(uploaded_resume.getbuffer())
                temp_path = temp_file.name

            resume_text = extract_resume_text(temp_path)

            similarity = calculate_similarity(
                jd_text,
                resume_text
            )

            skill_score, matched, missing = skill_match_score(
                jd_text,
                resume_text
            )

            ai_result = evaluate_candidate(
                jd_text,
                resume_text,
                similarity,
                matched,
                missing
            )

            final_score = (
                similarity * 0.7 +
                skill_score * 0.3
            )

            if final_score >= 0.85:
                recommendation = "Hire"

            elif final_score >= 0.70:
                recommendation = "Consider"

            else:
                recommendation = "Reject"

            results.append({

                "Candidate": uploaded_resume.name,

                "Similarity": round(similarity * 100, 2),

                "Skill Score": round(skill_score * 100, 2),

                "Final Score": round(final_score * 100, 2),

                "Matched Skills": ", ".join(matched),

                "Missing Skills": ", ".join(missing),

                "Recommendation": recommendation,

                "AI Evaluation": ai_result

            })

            os.remove(temp_path)

    # ---------------- Ranking ---------------- #

    results.sort(
        key=lambda x: x["Final Score"],
        reverse=True
    )

    df = pd.DataFrame(results)

    # ---------------- Dashboard ---------------- #

    st.header("Dashboard")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Candidates",
        len(df)
    )

    col2.metric(
        "Highest Score",
        f"{df['Final Score'].max():.1f}%"
    )

    col3.metric(
        "Average Score",
        f"{df['Final Score'].mean():.1f}%"
    )

    # ---------------- Ranking Table ---------------- #

    st.header("Candidate Rankings")

    st.dataframe(
        df[
            [
                "Candidate",
                "Final Score",
                "Similarity",
                "Skill Score",
                "Recommendation"
            ]
        ],
        use_container_width=True
    )

    # ---------------- Candidate Details ---------------- #

    st.header("Detailed Candidate Analysis")

    for candidate in results:

        with st.expander(
            f"{candidate['Candidate']} ({candidate['Final Score']}%)"
        ):

            st.progress(candidate["Final Score"] / 100)

            st.metric(
                "Final Score",
                f"{candidate['Final Score']:.1f}%"
            )

            st.subheader("Matched Skills")
            st.success(candidate["Matched Skills"])

            st.subheader("Missing Skills")
            st.error(candidate["Missing Skills"])

            if candidate["Recommendation"] == "Hire":
                st.success("Recommended for Interview")

            elif candidate["Recommendation"] == "Consider":
                st.warning("Consider")

            else:
                st.error("Reject")

            st.subheader("AI Evaluation")
            st.write(candidate["AI Evaluation"])

    # ---------------- Export ---------------- #

    csv_path = export_csv(results)
    json_path = export_json(results)

    st.header("Download Results")

    col1, col2 = st.columns(2)

    with col1:
        with open(csv_path, "rb") as f:
            st.download_button(
                "Download CSV",
                data=f,
                file_name="ranked_candidates.csv",
                mime="text/csv"
            )

    with col2:
        with open(json_path, "rb") as f:
            st.download_button(
                "Download JSON",
                data=f,
                file_name="ranked_candidates.json",
                mime="application/json"
            )