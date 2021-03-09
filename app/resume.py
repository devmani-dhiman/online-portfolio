import streamlit as st
import base64

def app():
    st.markdown("<h1 style='text-align: center; color: Purple;'>Resume</h1>", unsafe_allow_html=True)

    display_pdf(r"apps/Dev_resume.pdf")


def display_pdf(pdf_file):
    with open(pdf_file, 'rb') as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="800" height="2000" type="application/pdf">'
    st.markdown(pdf_display, unsafe_allow_html=True)