import streamlit as st
from langchain_groq import ChatGroq
from langchain_community.document_loaders import PyPDFLoader,TextLoader,Docx2txtLoader
st.set_page_config(
    page_title="AI RESUME REVIEWER",
    page_icon="🎓",
    layout="wide"
)
def extract_content(uploaded_file):
    
    file_extension = uploaded_file.name.split(".")[-1].lower()

    # Save uploaded file temporarily
    with open(uploaded_file.name, "wb") as f:
        f.write(uploaded_file.getvalue())

    if file_extension == "pdf":
        loader = PyPDFLoader(uploaded_file.name)

    elif file_extension == "txt":
        loader = TextLoader(uploaded_file.name, encoding="utf-8")

    elif file_extension == "docx":
        loader = Docx2txtLoader(uploaded_file.name)

    documents = loader.load()

    content = "\n".join(
        document.page_content for document in documents
    )

    return content


st.title("AI Resume Analyzer & Job Match Assistant")
st.write("Upload your resume,add a job description, and get a detailed analysis powered by AI!")
uploaded_file=st.file_uploader("Upload Your Resume",type=["pdf","docx","txt"])
job_description = st.text_area(
    "Enter Job Description",
    placeholder="Paste the job description here"
)
if uploaded_file is not None:
    st.success(f"Resume uploaded successfully")
groq_api_key="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"
with st.spinner("Analyze My Resume"):
    if uploaded_file is None:
        st.warning("Please upload your resume.")
    elif uploaded_file is not None:
        context=extract_content(uploaded_file)
        if context.strip():
            st.success("Content extracted successfully!")
            st.subheader("Extracted Content")
            st.text_area("Document Text",context,height=300)
    else:
        st.warning("Please provide context  or upload a document.")

if st.button("Analyze"):
    if not groq_api_key:
        st.error("Groq API key is missing")
    elif not context.strip():
        st.warning("Please provide context or upload a document.")
    else:
        try:
            llm = ChatGroq(
                model="openai/gpt-oss-20b",
                groq_api_key=groq_api_key,
                temperature=0.7
            )
            prompt=f"""
                You are an expert resume reviewer and career advisor.

                Analyze the following resume against the job description.

                RESUME:
                {context}

                JOB DESCRIPTION:
                {job_description}

                Provide the analysis using these sections:

                1. Candidate Profile Summary
                2. Technical Skills Identified
                3. Matched Skills
                4. Missing Skills
                5. Relevant Projects and Experience
                6. Resume Strengths
                7. Resume Weaknesses
                8. ATS Optimization Suggestions
                9. Recommendations to Improve Job Suitability

                Important:
                - Use only information available in the resume.
                - Do not invent qualifications or experience.
                - Clearly distinguish missing information from missing skills.
                - Do not invent a numerical job match score.
                - Give practical and specific suggestions.
                """
            response=llm.invoke(prompt)
            st.subheader("Resume Analysis")
            st.markdown(response.content)

        except Exception as e:
            st.error(f"Error : {e}")

