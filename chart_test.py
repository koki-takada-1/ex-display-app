import datetime
import pytz
import sys
import traceback
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

# 1990年以降の為替相場URL:定数
HISTORY_URL = 'http://www.murc-kawasesouba.jp/fx/past_3month.php'

# Chromeをインストール
driver_path = ChromeDriverManager().install()

#ブラウザを開く描写をしない
options = Options()
# options.add_argument('--headless')  
# options.add_argument('--disable-web-security')

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

manth_list=[1,2,3,4,5,6,7,8,9,10]
now = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))

d1 = datetime.datetime(2023,9,1)
d2 = datetime.datetime(2023,now.month,now.day)
diff = d2-d1

start_month = 6
tts_list = []
ttb_list = []

for i in range(diff.days):
    date = d1 + datetime.timedelta(i)
    # print(date)
    # print(date.month,type(date.month))
    # print(date.day,type(date.day))
    try:
        year_select.select_by_value('2023')
        manth_select.select_by_value(str(date.month))
        day_select.select_by_value(str(date.day))
        #　通貨コンボボックスのselect要素選択
        time.sleep(1)
        currency = WebDriverWait(driver, 10).until(lambda x: x.find_element(By.XPATH, '//*[@id="cc"]'))
        currency_select = Select(currency)
        currency_select.select_by_visible_text('米ドル')
    except Exception as e:
        etype, value, tb = sys.exc_info()
        print(traceback.format_exception(etype, value, tb))
        print("-"*20)
        print(e.__class__.__name__) # ZeroDivisionError
        print("-"*20)
        print(e.args) # ('division by zero',)
        print("-"*20)
        print(e) # division by zero
        print("-"*20)
        print(f"{e.__class__.__name__}: {e}") 
        print("-"*15 +"エラーの時の日付"+"-"*15)
        print(date)
        print(date.month,type(date.month))
        print(date.day,type(date.day))
        continue
    






    


