import streamlit as st
from streamlit_modal import Modal

if 'openmodel' not in st.session_state:
    st.session_state.openmodel = False
   
modal = Modal(key="Demo Key",title="test")
open_modal = st.button('open',key = 'rt')

if open_modal:
    st.session_state.openmodel = True
    
if st.session_state.openmodel:
    modal.open()
    
if modal.is_open():
    with modal.container():
        st.write('テキスト')
        st.write('テキスト')
        value = st.checkbox('check me')
# for col in st.columns(8):
#     with col:
#         open_modal = st.button(label='button',key='testbtn')
#         if open_modal:
#             with modal.container():
#                 st.markdown('testtesttesttesttesttesttesttest')