import streamlit as st
from streamlit_pdf_viewer import pdf_viewer
import base64

    # Convert to utf-8
with open("Thesis.pdf", "rb") as file:
    base64_pdf = base64.b64encode(file.read()).decode('utf-8')


pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>' 
st.markdown(pdf_display, unsafe_allow_html=True)