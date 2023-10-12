# 命名規則はPEP8に従う、文字列リテラルは''で統一
import datetime
import pytz

import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_modal import Modal
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

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
    
    with st.container():
     
        col1, col2 = st.columns(2)
        with col1:
            df = pd.read_csv('usd.csv')
            fig = px.line(df,x='date',y=['tts','ttb'],title="USD 4-Moth Chart")
            st.plotly_chart(fig, use_container_width=True)

        with col2:
            st.markdown("#### 三菱UFJ銀行公表相場　 2023年10月12日 現在")
            st.image("kawase.png")

# うるう年判定関数
# 400で割り切れる　または　(100で割り切れない かつ 4で割り切れる)
def leep_year(year):
    return year % 400 == 0 or (year % 100 != 0 and year % 4 == 0)

def setting_days(year,month,days_max):
    if month == 2:
        if leep_year(year):
            return ['----'] + list(range(1,29+1))
        else:
            return ['----'] + list(range(1,28+1))
    else:
        return ['----'] + list(range(1,days_max[month+1]+1))
            
        

def sidebar_display():
    # 今現在の時間取得
    now = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))

    # 三菱UFJ銀行から取得できる為替相場は1990年以降のもの
    start_year = 1990

    # 今現在の西暦取得,int型
    now_year = now.year
    
    # 未選択
    unselect = ['----']

    # 選択できる西暦リスト作成
    years = unselect + list(range(start_year,now_year+1))

    # 月リスト作成
    month = unselect + list(range(1,13))

    # 月ごとの日数リスト作成
    days_max = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # 西暦と月を選択する前の日にち初期リスト
    days = ['----']
    st.sidebar.markdown('## 過去の為替情報')
    # コンボボックス、検索ボタン配置
    year_selector = st.sidebar.selectbox('年',years)
    month_selector = st.sidebar.selectbox('月',month)
    # day_selector = st.sidebar.selectbox('日',days)
    

    # 西暦と月が選択されたかどうかで日にちリスト更新
    
 
    if year_selector != unselect[0] and month_selector != unselect[0]:
        days = setting_days(year_selector,month_selector,days_max)
        day_selector = st.sidebar.selectbox('日',days)
        search_btn = st.sidebar.button('検索')
        
        
        if search_btn:
            if year_selector != unselect[0] and month_selector != unselect[0] and day_selector != unselect[0]:
                st.markdown('検索ボタンが押されました')
            else:
                st.markdown('### 西暦、月、日を全て選択してください')  
                

        else:
            pass




spred = 149.12 - 148.62
main_page(149.12,spred)
sidebar_display()





