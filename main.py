import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

driver_path = "C:/Users/ayamu/python programs/drivers/chromedriver-win64/chromedriver.exe" 

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-cookies")
chrome_options.add_argument("--enable-gpu")
chrome_options.add_argument("--no-sandbox")

driver = webdriver.Chrome(service=Service(driver_path), options=chrome_options)

def get_about(urls):
    for url in urls:
        company = url.replace("https://www.linkedin.com/company/", "").replace("/about/", "")

        driver.get(url)
        username_tag = driver.find_element(By.ID, "username")
        username_tag.send_keys("jenese1987@noefa.com")

        time.sleep(1)
        password_tag = driver.find_element(By.ID, "password")
        password_tag.send_keys("1234@password")

        sign_in_button = driver.find_element(By.XPATH, "//button[@aria-label='Sign in']")
        sign_in_button.click()
        time.sleep(2)

        p_tag = driver.find_element(By.CSS_SELECTOR, "p.white-space-pre-wrap")
        with open(f"{company}.txt", "x") as f:
            f.write(p_tag.text)
            f.close()
        driver.quit()

url = ["https://www.linkedin.com/company/hyrgpt/about/"]

get_about(url)