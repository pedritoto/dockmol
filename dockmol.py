import streamlit as st
from openbabel import pybel

from stmol import showmol
import py3Dmol

import subprocess
subprocess.call('rm /app/dockmol/*.pdb', shell=True)

st.title("inicio")     
# Using object notation
prot_pdb_or = st.sidebar.selectbox(
    "Elige origen del archivo pdb?",
    ("PDB ID", "From PC")
)
if prot_pdb_or == "PDB ID":
    st.text_input('PDB ID', value="", max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, args=None, kwargs=None, placeholder=None, disabled=False)



with st.sidebar:
    prot_pdb_uploaded=st.file_uploader("sube pdb", type='pdb', accept_multiple_files=False, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False)
    if prot_pdb_uploaded is not None:
        prot_pdb_name=prot_pdb_uploaded.name
        with open(prot_pdb_name,'wb') as f:
            f.write(prot_pdb_uploaded.getbuffer())
        #mol = pybel.readfile("pdb",prot_pdb_name)
        pdbview = py3Dmol.view()
        pdbview.addModel(open(prot_pdb_name, 'r').read(),'pdb')
        pdbview.setStyle({'stick':{}})
        pdbview.zoomTo()
        showmol(pdbview, height = 500,width=800)
 
   

#lines=open(prot_pdb_name, 'r').read()
#lines



#subprocess.call('cat /app/dockmol/1tqn.pdb', shell=True)
subprocess.call('ls /app/dockmol/', shell=True)