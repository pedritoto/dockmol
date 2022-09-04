import streamlit as st
from openbabel import pybel

from stmol import showmol
import py3Dmol

st.title("inicio")     
from io import StringIO
prot_pdb_uploaded=st.file_uploader("sube pdb", type='pdb', accept_multiple_files=False, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False)
if prot_pdb_uploaded is not None:
    with open(prot_pdb_uploaded.name,'wb') as f:
        f.write(prot_pdb_uploaded.getbuffer())
        mol = pybel.readfile("pdb",prot_pdb_uploaded.name)
        # 1A2C
        # Structure of thrombin inhibited by AERUGINOSIN298-A from a BLUE-GREEN ALGA
    xyzview = py3Dmol.view(prot_pdb_uploaded.name) 
    xyzview.setStyle('licorice')
    showmol(xyzview, height = 500,width=800)






import subprocess
subprocess.call('ls /app/dockmol/', shell=True)