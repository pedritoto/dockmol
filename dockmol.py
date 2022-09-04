import streamlit as st
from openbabel import pybel
st.title("inicio")     
from io import StringIO
fileup=st.file_uploader("sube pdb", type=None, accept_multiple_files=True, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False)
#if fileup is not None:
#    stringio = StringIO(fileup.getvalue().decode("utf-8"))
#    st.write(stringio)
for uploaded_file in fileup:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)
#file=st.file_uploader("sube pdb", type=None, accept_multiple_files=True, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False)
st.write(fileup)
#mol = pybel.readfile("pdb", "water.pdb")
import subprocess

cmd = "pwd "

subprocess.call(cmd, shell=True)

subprocess.call('ls /app/dockmol/', shell=True)