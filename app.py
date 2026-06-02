import streamlit as st
import vertexai
from vertexai.generative_models import GenerativeModel

# 1. Initialize Vertex AI (No API key needed! It authenticates automatically via Cloud Run)
# I have securely hardcoded your specific Project ID and region here.
vertexai.init(project="gen-lang-client-0666924346", location="us-central1")

# Vertex AI uses a slightly different naming convention for models
model = GenerativeModel('gemini-2.5-flash')

st.set_page_config(page_title="AI Code Reviewer", page_icon="💻", layout="wide")
st.title("💻 AI-Powered Code Reviewer (Enterprise Edition)")
st.write("Running securely without API keys on Google Cloud Vertex AI.")

language = st.selectbox(
    "What language is this code written in?",
    ("Python", "C", "JavaScript", "HTML/CSS", "Other")
)

uploaded_file = st.file_uploader("Upload a code file", type=["py", "c", "js", "html", "css", "txt"])
user_code = ""

if uploaded_file is not None:
    user_code = uploaded_file.getvalue().decode("utf-8")
    st.success("File uploaded successfully!")
    with st.expander("View Uploaded Code"):
        st.code(user_code, language=language.lower())
else:
    user_code = st.text_area("Or paste your code here:", height=250)

if st.button("Review My Code"):
    if user_code:
        with st.spinner("Analyzing your code via Vertex AI..."):
            prompt = f"""
            You are an expert senior software developer specializing in {language}. 
            Review the following code and provide:
            1. A brief summary of its purpose.
            2. Identification of any bugs, logic errors, or syntax issues.
            3. Suggestions for improving efficiency, memory management, and readability.
            
            Here is the code:
            \n\n{user_code}
            """
            
            # Send to Vertex AI
            response = model.generate_content(prompt)
            
            st.subheader("Review & Feedback")
            st.write(response.text)
    else:
        st.warning("Please upload a file or enter some code first!")