import streamlit as st

def history_page_display(csv,html):
    st.download_button(
        label="CSVダウンロード",
        data=csv,
        file_name='table.csv',
        mime='text/csv',
        key="download-tools-csv"
    )

    st.markdown(html,unsafe_allow_html=True)
    st.markdown('何月何日の為替相場')