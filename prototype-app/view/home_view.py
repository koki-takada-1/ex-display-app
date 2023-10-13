
import streamlit as st
import pandas as pd
import plotly.express as px

def main_page(rate,spread,img):
    st.set_page_config(layout="wide")
    with st.container():
        st.markdown('### 最終更新日時：2023年10月11日 13時10分')
        st.markdown('## 米ドルTTS リアルタイムレート')
        st.markdown(f'<p style= "color:black;\
                    font-size:40px;\
                    border: 0.15rem solid;\
                    writing-mode: horizontal-tb;\
                    text-align: center;\
                    border-radius: 10px; \
                    "p>{rate}\
                    </p>',unsafe_allow_html=True
        )
        
        st.markdown(f'## スプレッド')
        st.markdown(f'<p style= "color:black;\
                    font-size:40px;\
                    border: 0.15rem solid;\
                    writing-mode: horizontal-tb;\
                    text-align: center;\
                    border-radius: 10px; \
                    "p>{spread}\
                    </p>',unsafe_allow_html=True
        )
    
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            df = pd.read_csv('usd.csv')
            fig = px.line(df,x='date',y=['tts','ttb'],title="USD 4-Moth Chart")
            st.plotly_chart(fig, use_container_width=True)

        with col2:
            st.markdown("#### 三菱UFJ銀行公表相場　 2023年10月12日 現在")
            st.image(img)