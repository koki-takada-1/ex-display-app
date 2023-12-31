import datetime
import pytz
import time
import pandas as pd

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


now = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))

d1 = datetime.datetime(2023,7,1)
d2 = datetime.datetime(2023,now.month,now.day)
diff = d2-d1

tts_list = []
ttb_list = []
date_list = []

for i in range(diff.days):

    date = d1 + datetime.timedelta(i)
    try:
        year_select.select_by_value('2023')
        manth_select.select_by_value(str(date.month))
        day_select.select_by_value(str(date.day))
        time.sleep(1)
        #　通貨コンボボックスのselect要素選択
        currency = WebDriverWait(driver, 10).until(lambda x: x.find_element(By.XPATH, '//*[@id="cc"]'))
        currency_select = Select(currency)
        currency_select.select_by_visible_text('米ドル')
    except Exception as e:
        print(e)
        continue
    # 検索ボタンをクリック
    decide_btn.click()
    time.sleep(3)
    
    # ウィンドウリスト
    window_list = driver.window_handles
    # 検索した通貨のウィンドウに遷移した後に、ドライバーを遷移したウィンドウに切り替える
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(2)
    tts = WebDriverWait(driver, 10).until(lambda x: x.find_element(By.XPATH, '/html/body/div[1]/table/tbody/tr[2]/td[4]'))
    ttb = WebDriverWait(driver, 10).until(lambda x: x.find_element(By.XPATH, '/html/body/div[1]/table/tbody/tr[2]/td[5]'))
    
    tts_list.append(float(tts.text))
    ttb_list.append(float(ttb.text))
    date_list.append(date.date())
    driver.close()
    driver.switch_to.window(driver.window_handles[0])

usd_df = pd.DataFrame({'date':date_list,'tts':tts_list,'ttb':ttb_list})

usd_df.to_csv('usd.csv')





    


