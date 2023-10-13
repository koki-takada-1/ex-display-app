import streamlit as st

from view import home_view
from view import sidebar_view

import scraper 

def main():
    if 'root' not in st.session_state:
        st.session_state.root = 'done'
        st.session_state.control = scraper.Scraper()
       
        ex_info = st.session_state.control.realtime_info()
        st.session_state.tts = ex_info['tts']
        st.session_state.spread = ex_info['spread']

        st.session_state.img = st.session_state.control.chart_img_get()

    st.session_state.sidebar = sidebar_view.Sidebar_view(st.session_state.control)
    home_view.main_page(st.session_state.tts,st.session_state.spread,st.session_state.img)
    st.session_state.sidebar.sidebar_display()

if __name__ == "__main__":
    main()