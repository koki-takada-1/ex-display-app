import datetime
import pytz

import streamlit as st
import streamlit.components.v1 as components
from view import his_page
import scraper

class Sidebar_view:
    def __init__(self,init_control) -> None:
        # scraperオブジェクト
        self.init_control = init_control
        # 未選択
        self.UNSELECT = ['--']
        # 三菱UFJ銀行から取得できる為替相場は1990年以降のもの
        self.START_YEAR = 1990
        # 各月の日数
        self.DAYS_MAX = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # 検索ボタンが押されたときの処理(コールバック関数)
    def colled_search(self,year,month,day):
        if year != self.UNSELECT[0] and month != self.UNSELECT[0] and day != self.UNSELECT[0]:
            his_dict = self.init_control.search_history(year,month,day)
            if his_dict == 'error':
                components.html('<script> alert("選択された年月日には、データが存在しません");</script>')
            else:
                his_page.history_page_display(his_dict['csv'],his_dict['table_html'])
        else:
            components.html('<script> alert("未選択の項目があります。西暦、月、日付すべて選択してください。");</script>')

    # うるう年判定メソッド
    def leep_year(self,year):
        return year % 400 == 0 or (year % 100 != 0 and year % 4 == 0)

    def setting_days(self,year,month):
        # 2月が選択されたならば
        if month == 2:
            if self.leep_year(year):
                # うるう年ならば29日までオプション作成
                return ['--'] + list(range(1,29+1))
            else:
                # うるう年でなければ28日までオプション作成
                return ['--'] + list(range(1,28+1))
        else:
            # 2月が選択されていなければ、DAYS_MAXの(month+1)番目までオプション作成
            return ['--'] + list(range(1,self.DAYS_MAX[month+1]+1))
        
    def sidebar_display(self):
        # 今現在の時間取得
        now = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))

        # 今現在の西暦取得,int型
        now_year = now.year

        # 選択できる西暦リスト作成
        years = self.UNSELECT + list(range(self.START_YEAR,now_year+1))

        # 月リスト作成
        month = self.UNSELECT + list(range(1,13))

        # 西暦と月を選択する前の日にち初期リスト
        days = ['--']
        st.sidebar.markdown('## 過去の為替情報')
        # コンボボックス、検索ボタン配置
        year_selector = st.sidebar.selectbox('年',years)
        month_selector = st.sidebar.selectbox('月',month)

        # 西暦と月が選択されたかどうかで日付セレクトボックス表示
        if year_selector != self.UNSELECT[0] and month_selector != self.UNSELECT[0]:
            days = self.setting_days(year_selector,month_selector)
            day_selector = st.sidebar.selectbox('日',days)
            # 検索ボタン配置、押された時の処理をon_cllickに登録
            s_btn = st.sidebar.button('検索')
            if s_btn:
                self.colled_search(year_selector,month_selector,day_selector)
            else:
                pass
            
            
        