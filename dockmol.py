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
prot_show = False
lig_show = False


with st.sidebar:
    with st.expander("Protein"):
        prot_pdb_or = st.selectbox("Protein PDB source?",("PDB ID", "From PC"))
        if prot_pdb_or == "PDB ID":
            prot_pdb_id=st.text_input('PDB ID', value="", max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, args=None, kwargs=None, placeholder=None, disabled=False)
            if prot_pdb_id != '':
                #prot_pdb_name=prot_pdb_id+'.pdb'
                prot_pdb_name='protein.pdb'
                prot_pdb_content = get_pdb_file(prot_pdb_id, filetype='pdb', compression=False)
                with open(prot_pdb_name,'w') as f:
                    print(prot_pdb_content,file=f)
                    st.success(prot_pdb_name+' created succesfully')
                    if prot_show:
                        prot_show=st.button('Hide protein', key=None, help='Hides 3D model of protein', on_click=None, args=None, kwargs=None, disabled=False)
                    else:    
                        prot_show=st.button('Show protein', key=None, help='displays 3D model of protein', on_click=None, args=None, kwargs=None, disabled=False)
                    


        else:
            prot_pdb_uploaded=st.file_uploader("Upload PDB file", type='pdb', accept_multiple_files=False, key='pu', help=None, on_change=None, args=None, kwargs=None, disabled=False)
            if prot_pdb_uploaded is not None:
                #prot_pdb_name=prot_pdb_uploaded.name
                prot_pdb_name='protein.pdb'
                with open(prot_pdb_name,'wb') as f:
                    f.write(prot_pdb_uploaded.getbuffer()) 
                    st.success(prot_pdb_name+' created sussesfully')
                    if prot_show:
                        prot_show=st.button('Hide protein', key=None, help='Hides 3D model of protein', on_click=None, args=None, kwargs=None, disabled=False)
                    else:    
                        prot_show=st.button('Show protein', key=None, help='displays 3D model of protein', on_click=None, args=None, kwargs=None, disabled=False)
                    

    with st.expander("Ligand"):         
        lig_pdb_uploaded=st.file_uploader("Upload PDB file", type='pdb', accept_multiple_files=False, key='lu', help=None, on_change=None, args=None, kwargs=None, disabled=False)
        if lig_pdb_uploaded is not None:
            lig_pdb_name='ligand.pdb'
            with open(lig_pdb_name,'wb') as f:
                f.write(lig_pdb_uploaded.getbuffer()) 
                st.success(lig_pdb_name+' creado')
                if lig_show:
                    lig_show=st.button('Hide ligand', key=None, help='Hides 3D model of ligand', on_click=None, args=None, kwargs=None, disabled=False)
                else:    
                    lig_show=st.button('Show ligand', key=None, help='displays 3D model of ligand', on_click=None, args=None, kwargs=None, disabled=False)
                #lig_show=st.button('Show molecule', key=None, help='displays 3D model of ligand', on_click=None, args=None, kwargs=None, disabled=False)
 
   

#lines=open(prot_pdb_name, 'r').read()
#lines

if prot_show:
    protview = py3Dmol.view()
    protview.addModel(open(prot_pdb_name, 'r').read(),'pdb')
    protview.setStyle({'cartoon':{'color':'spectrum'}})
    protview.zoomTo()
    showmol(protview, height = 500,width=800)
if lig_show:
    ligview = py3Dmol.view()
    ligview.addModel(open(lig_pdb_name, 'r').read(),'pdb')
    ligview.setStyle({'stick':{}})
    ligview.zoomTo()
    showmol(ligview, height = 500,width=800)



#subprocess.call('cat /app/dockmol/1tqn.pdb', shell=True)
#
subprocess.call('echo +++++++++++++++++++++++++++++++++++++++', shell=True)
subprocess.call('echo +++++++++++++++++++++++++++++++++++++++', shell=True)
subprocess.call('ls /app/dockmol/', shell=True)
#if prot_pdb_name != '':
#    subprocess.call('cat /app/dockmol/'+prot_pdb_name, shell=True)
#                subprocess.call('echo ++++++++++++ SUBIDO ++++++++++++++++++', shell=True)
#                subprocess.call('head /app/dockmol/'+prot_pdb_name, shell=True)
#                subprocess.call('echo ---------------------------------------', shell=True)
#                subprocess.call('ls /app/dockmol/', shell=True)
#                subprocess.call('echo -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-', shell=True)    
#          pdbview = py3Dmol.view()
#          pdbview.addModel(open(prot_pdb_name, 'r').read(),'pdb')
#          pdbview.setStyle({'stick':{}})
#          pdbview.zoomTo()
#          showmol(pdbview, height = 500,width=800)