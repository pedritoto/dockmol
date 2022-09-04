import streamlit as st
from openbabel import pybel
st.title("inicio")     
stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
st.write(stringio)

#file=st.file_uploader("sube pdb", type=None, accept_multiple_files=True, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False)
3st.write(file)
#mol = pybel.readfile("pdb", "water.pdb")
import subprocess

cmd = "ls "

subprocess.call(cmd, shell=True)

