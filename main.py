import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

driver_path = "C:/Users/ayamu/python-programs/drivers/chromedriver-win64/chromedriver.exe" 

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--ignore-certificate-errors") 
chrome_options.add_argument("--disable-cookies")
chrome_options.add_argument("--enable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--remote-debugging-port=9222")

driver = webdriver.Chrome(service=Service(driver_path), options=chrome_options)

def get_about(linkedin_url):
    for url in linkedin_url:
        company = url.replace("https://www.linkedin.com/company/", "").replace("/about/", "").replace('/','')

        driver.get(url)
        time.sleep(random.uniform(2, 5))
        text = driver.find_element(By.XPATH, '''//*[@id="main-content"]/section[1]/div/section[1]/div/p''').text
        print(text)
        with open(f"{company}.txt", "x") as f:
            f.write(text)
            f.close()
        driver.quit()


url = ["https://www.linkedin.com/company/opkey"]
get_about(url)