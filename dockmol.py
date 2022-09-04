import streamlit as st
from openbabel import pybel

from stmol import showmol
import py3Dmol

st.title("inicio")     
from io import StringIO
prot_pdb_uploaded=st.file_uploader("sube pdb", type='pdb', accept_multiple_files=False, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False)
if prot_pdb_uploaded is not None:
    prot_pdb_name=prot_pdb_uploaded.name
    with open(prot_pdb_name,'wb') as f:
        f.write(prot_pdb_uploaded.getbuffer())
        #mol = pybel.readfile("pdb",prot_pdb_name)
        # 1A2C
        # Structure of thrombin inhibited by AERUGINOSIN298-A from a BLUE-GREEN ALGA
 
   
pdbview = py3Dmol.view()
pdbview.addModel(open('1tqn.pdb', 'r').read(),'pdb')
pdbview.setStyle({'cartoon':{}})
showmol(pdbview, height = 500,width=800)
#lines=open(prot_pdb_name, 'r').read()
#lines


import subprocess
subprocess.call('cat /app/dockmol/1tqn.pdb', shell=True)