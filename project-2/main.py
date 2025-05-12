# made projects using  google open source ai api 

import streamlit as st 

import PyPDF2
import io
import os
from openai import OpenAI   
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title = "AI resume crtiquer" , page_icon = "🤖", layout = "centered")

st.title("AI Resume Critiquer")
st.markdown("Upload your resume in PDF format and get feedback on how to improve it.")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

uploaded_file = st.file_uploader("Upload your resume", type=["pdf"])

job_role = st.text_input("enter the job role you you're  taregetting (optional)")

analyze = st.button("Analyze Resume")


if analyze:
    st.write("button pressed")
