import streamlit as st
from streamlit_pdf_viewer import pdf_viewer



pdf_viewer("Thesis.pdf",
           rendering='unwrap')