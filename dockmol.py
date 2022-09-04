import streamlit as st
from openbabel import pybel

from stmol import showmol
import py3Dmol
from pypdb import *
import subprocess
subprocess.call('rm -rf /app/dockmol/*.pdb', shell=True)

st.title("inicio")     
# Using object notation
prot_pdb_name=''
prot_pdb_id=''


with st.sidebar:
    with st.expander("Protein"):
        prot_pdb_or = st.selectbox("Elige origen del archivo pdb?",("PDB ID", "From PC"))
        if prot_pdb_or == "PDB ID":
            prot_pdb_id=st.text_input('PDB ID', value="", max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, args=None, kwargs=None, placeholder=None, disabled=False)
            if prot_pdb_id != '':
                prot_pdb_name=prot_pdb_id+'.pdb'
                prot_pdb_content = get_pdb_file(prot_pdb_id, filetype='pdb', compression=False)
                with open(prot_pdb_name,'w') as f:
                    print(prot_pdb_content,file=f)
                    st.success(prot_pdb_name+' creado', icon:":check:")


        else:
            prot_pdb_uploaded=st.file_uploader("sube pdb", type='pdb', accept_multiple_files=False, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False)
            if prot_pdb_uploaded is not None:
                prot_pdb_name=prot_pdb_uploaded.name
                with open(prot_pdb_name,'wb') as f:
                    f.write(prot_pdb_uploaded.getbuffer()) 
                    st.success(prot_pdb_name+' creado', icon:":check:")
             

#          pdbview = py3Dmol.view()
#          pdbview.addModel(open(prot_pdb_name, 'r').read(),'pdb')
#          pdbview.setStyle({'stick':{}})
#          pdbview.zoomTo()
#          showmol(pdbview, height = 500,width=800)
 
   

#lines=open(prot_pdb_name, 'r').read()
#lines



#subprocess.call('cat /app/dockmol/1tqn.pdb', shell=True)
#subprocess.call('ls /app/dockmol/', shell=True)
#subprocess.call('echo +++++++++++++++++++++++++++++++++++++++', shell=True)
#subprocess.call('echo +++++++++++++++++++++++++++++++++++++++', shell=True)
#if prot_pdb_name != '':
#    subprocess.call('cat /app/dockmol/'+prot_pdb_name, shell=True)
#                subprocess.call('echo ++++++++++++ SUBIDO ++++++++++++++++++', shell=True)
#                subprocess.call('head /app/dockmol/'+prot_pdb_name, shell=True)
#                subprocess.call('echo ---------------------------------------', shell=True)
#                subprocess.call('ls /app/dockmol/', shell=True)
#                subprocess.call('echo -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-', shell=True)    