# 命名規則はPEP8に従う、文字列リテラルは''で統一

import streamlit as st



def sidebar_display():
    st.sidebar.markdown('## 過去の為替情報')
    st.sidebar.selectbox('年',(2023,2022,2021,2020))
    st.sidebar.selectbox('月',(1,2,3,4,5,6,7,8,9,10,11,12))
    st.sidebar.selectbox('日',(1,2,3,4,5))

    #-----------セレクトボックスここまで---------------

    # もし、8月を選択したら30日まで、9月を選択したら31を表示する。

def main_page(rate,spread):
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


spred = 149.12 - 148.62

sidebar_display()
main_page(149.12,spred)

# css injection


