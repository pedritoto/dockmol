import streamlit as st
from openbabel import pybel
st.title("inicio")     
from io import StringIO
prot_pdb_uploaded=st.file_uploader("sube pdb", type='pdb', accept_multiple_files=False, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False)
if prot_pdb_uploaded is not None:
    with open(prot_pdb_uploaded.name,'wb') as prot_pdb_name:
        prot_pdb_name.write(prot_pdb_uploaded.getbuffer())
        mol = pybel.readfile("pdb",prot_pdb_name)
import subprocess

cmd = "pwd "

subprocess.call(cmd, shell=True)

subprocess.call('ls /app/dockmol/', shell=True)