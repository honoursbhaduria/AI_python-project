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

