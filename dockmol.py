import streamlit as st
from openbabel import pybel
st.title("inicio")     
from io import StringIO
prot_pdb=st.file_uploader("sube pdb", type='pdb', accept_multiple_files=True, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False)
if prot_pdb is not None:
#    bytes_data = fileup.readlines()
#    st.write("filename:", uploaded_file.name)
    with open(prot_pdb.name,'wb') as f:
        f.write(prot_pdb.getbuffer())
    #print('------------',bytes_data) #, file=uploaded_file.name)

#mol = pybel.readfile("pdb",uploaded_file.name)
import subprocess

cmd = "pwd "

subprocess.call(cmd, shell=True)

subprocess.call('ls /app/dockmol/', shell=True)