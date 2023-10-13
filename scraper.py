import requests
from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class Scraper:
    def __init__(self) -> None:
        # 1990年以降の為替相場URL:定数
        self.HISTORY_URL = 'http://www.murc-kawasesouba.jp/fx/past_3month.php'
        
        # 外国為替相場一覧表（リアルタイムレート)URL:定数
        self.REALTIME_URL = 'https://www.bk.mufg.jp/ippan/rate/real.html'

        # 今月を含めた5カ月のチャート画像があるURL:定数
        self.CHARTIMG_URL = 'http://www.murc-kawasesouba.jp/fx/index.php' 
        
        # スプレッド
        self.spread = 0
        
        # Chromeをインストール
        driver_path = ChromeDriverManager().install()

        #ブラウザを開く描写をしない
        options = Options()
        options.add_argument('--headless')  
        options.add_argument('--disable-web-security')

        # ブラウザをChromeに設定
        self.driver = webdriver.Chrome(service=Service(executable_path=driver_path),options=options)
    
    def chart_img_get(self):
        # 画像のXPath
        RATE_IMG = '//*[@id="main"]/div[3]/p[2]/img'

        # 今月を含めた5カ月のチャート画像があるサイトにアクセス
        self.driver.get(self.CHARTIMG_URL)
        img_element = WebDriverWait(self.driver, 10).until(lambda x: x.find_element(By.XPATH, RATE_IMG))
        # Web上の画像URLを取得
        img_url = img_element.get_attribute("src")
        print(img_url)

        # 画像要素取得
        img_content = requests.get(img_url).content

        with open("kawase.png", "wb") as w:
                w.write(img_content)

        image = Image.open("kawase.png")
        
        return image
    
    def realtime_info(self) -> dict:
        # REALTIME_URL:TTS(日本円→外貨)の値のXPath
        USD_TTS_PATH = '/html/body/div[1]/div/div/div[2]/main/article/div/div[1]/div/table/tbody/tr[1]/td[1]'

        # TTB(外貨→日本円)
        USD_TTB_PATH = '/html/body/div[1]/div/div/div[2]/main/article/div/div[1]/div/table/tbody/tr[1]/td[2]'

        # リアルタイムレートサイトにアクセス
        self.driver.get(self.REALTIME_URL)
        
        tts_element = WebDriverWait(self.driver, 10).until(lambda x: x.find_element(By.XPATH, USD_TTS_PATH))
        ttb_element = WebDriverWait(self.driver, 10).until(lambda x: x.find_element(By.XPATH, USD_TTB_PATH))

        

        tts = float(tts_element.text)
        ttb = float(ttb_element.text)
        spread = tts - ttb

        return { 'tts':tts_element.text, 'spread': spread}
    

    
