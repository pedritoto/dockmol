import streamlit as st
from openbabel import pybel
st.title("inicio")     
from io import StringIO
fileup=st.file_uploader("sube pdb", type=None, accept_multiple_files=True, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False)
#if fileup is not None:
#    stringio = StringIO(fileup.getvalue().decode("utf-8"))
#    st.write(stringio)

#file=st.file_uploader("sube pdb", type=None, accept_multiple_files=True, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False)
st.write(file)
#mol = pybel.readfile("pdb", "water.pdb")
import subprocess

cmd = "pwd "

subprocess.call(cmd, shell=True)

