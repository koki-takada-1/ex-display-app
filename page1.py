import time
import pandas as pd
import streamlit as st

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

import csv
import urllib
from bs4 import BeautifulSoup

frame = []
# もし一回もスクレイピングしてないならば(読み込み一回目ならば)
if 'scrape' not in st.session_state:

    # スクレイピングした印
    st.session_state.scrape = 'done'

    # 1990年以降の為替相場URL:定数
    HISTORY_URL = 'http://www.murc-kawasesouba.jp/fx/past_3month.php'

    # Chromeをインストール
    driver_path = ChromeDriverManager().install()

    #ブラウザを開く描写をしない
    options = Options()
    options.add_argument('--headless')  
    options.add_argument('--disable-web-security')

    # ブラウザをChromeに設定
    driver = webdriver.Chrome(service=Service(executable_path=driver_path),options=options)

    driver.get(HISTORY_URL)


    # 西暦
    year = WebDriverWait(driver, 10).until(lambda x: x.find_element(By.XPATH, '//*[@id="yy"]'))

    # 月
    month = WebDriverWait(driver, 10).until(lambda x: x.find_element(By.XPATH, '//*[@id="mm"]'))

    # 日
    day = WebDriverWait(driver, 10).until(lambda x: x.find_element(By.XPATH, '//*[@id="dd"]'))



    decide_btn = WebDriverWait(driver, 10).until(lambda x: x.find_element(By.XPATH, '//*[@id="sbmt"]'))

    year_select = Select(year)

    manth_select = Select(month)

    day_select = Select(day)




    year_select.select_by_value('2023')
    manth_select.select_by_value(str(10))
    day_select.select_by_value(str(11))
    time.sleep(1)
    #　通貨コンボボックスのselect要素選択
    currency = WebDriverWait(driver, 10).until(lambda x: x.find_element(By.XPATH, '//*[@id="cc"]'))
    currency_select = Select(currency)
    currency_select.select_by_visible_text('--')
    decide_btn.click()
    time.sleep(3)
        
    # ウィンドウリスト
    window_list = driver.window_handles
    # 検索した通貨のウィンドウに遷移した後に、ドライバーを遷移したウィンドウに切り替える
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(2)
    table = WebDriverWait(driver, 10).until(lambda x: x.find_element(By.XPATH, '/html/body/div[1]/table'))

    html=table.get_attribute("outerHTML")
    st.session_state.html = html

    c_table = BeautifulSoup(html, 'html.parser')
    rows = c_table.find_all("tr")

    for row in rows:
        csvRow = []
        for cell in row.findAll(['td', 'th']):
            csvRow.append(cell.get_text())
        frame.append(csvRow)

    df = pd.DataFrame(frame)
    csv=df.to_csv(index=False).encode('utf_8_sig')
    st.session_state.csv = csv

st.download_button(
    label="CSVダウンロード",
    data=st.session_state.csv,
    file_name='table.csv',
    mime='text/csv',
    key="download-tools-csv"
)

st.markdown(st.session_state.html,unsafe_allow_html=True)


        
