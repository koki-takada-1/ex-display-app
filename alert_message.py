import streamlit as st
from streamlit_modal import Modal
import streamlit.components.v1 as components

components.html('<script> alert("未選択の項目があります。西暦、月、日付すべて選択してください。");</script>')
# components.html('<script> alert("選択された年月日には、データが存在しません");</script>')
