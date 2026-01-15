import streamlit as st
import os
from dotenv import load_dotenv

from ingest import load_java_files
from chunk import chunk_by_file
from embed import build_vector_store
from retrieve import get_relevant_chunks
from generate import generate_answer

# --------------------------------------------------
# Load environment variables (.env)
# --------------------------------------------------
load_dotenv()

# --------------------------------------------------
# Streamlit Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Bahmni Legacy Modernization Intelligence",
    layout="wide"
)

st.title("🏥 Bahmni Legacy Code Modernization Assistant")

st.markdown(
    """
    This tool analyzes the **Bahmni-Core legacy Java healthcare system** and helps:

    - Understand embedded business & medical rules  
    - Discover workflows and dependencies  
    - Reduce risk during legacy modernization  

    **Note:**  
    This is **not a chatbot**.  
    It is an **AI-powered legacy system understanding engine**.
    """
)

# --------------------------------------------------
# Sidebar Configuration
# --------------------------------------------------
with st.sidebar:
    st.header("Configuration")

    repo_path = st.text_input(
        "Local path to Bahmni-Core repository",
        placeholder=r"D:\bahmni_rag_project\bahmni-core"
    )

    if os.getenv("SARVAM_API_KEY"):
        st.success("Sarvam API key loaded from .env")
    else:
        st.error("SARVAM_API_KEY not found. Check your .env file.")

    build_btn = st.button("Build Knowledge Base")

# --------------------------------------------------
# Build Knowledge Base
# --------------------------------------------------
if build_btn:
    if not os.getenv("SARVAM_API_KEY"):
        st.error("SARVAM_API_KEY missing in environment.")
    elif not repo_path or not os.path.isdir(repo_path):
        st.error("Invalid Bahmni-Core repository path.")
    else:
        with st.spinner("Scanning legacy Java files..."):
            java_files = load_java_files(repo_path)

        with st.spinner("Creating semantic documents..."):
            docs = chunk_by_file(java_files)

        with st.spinner("Building vector store (FAISS + embeddings)..."):
            vectorstore = build_vector_store(docs)

        st.session_state["vectorstore"] = vectorstore
        st.success("Knowledge base built successfully!")

# --------------------------------------------------
# Question & Analysis Section
# --------------------------------------------------
if "vectorstore" in st.session_state:
    st.markdown("---")
    st.subheader("Ask Questions About the Legacy System")

    question = st.text_input(
        "Your question",
        placeholder="e.g. What are the rules for patient registration?"
    )

    if st.button("Analyze"):
        if not question.strip():
            st.warning("Please enter a question.")
        else:
            with st.spinner("Retrieving relevant legacy code..."):
                chunks = get_relevant_chunks(
                    st.session_state["vectorstore"],
                    question
                )

            with st.spinner("Analyzing with Sarvam AI..."):
                answer = generate_answer(question, chunks)

            st.markdown("### 🧠 Answer")
            st.write(answer)
else:
    st.info("Build the knowledge base first to start analysis.")
