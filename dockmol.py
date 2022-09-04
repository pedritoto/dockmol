import streamlit as st
from openbabel import pybel
st.title("inicio")
st.file_uploader("sube pdb", type=None, accept_multiple_files=True, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False)
mol = pybel.readfile("pdb", "water.pdb")
