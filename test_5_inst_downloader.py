import time

import wget
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

option = Options()
option.add_argument("--disable-blink-features=AutomationControlled")
#option.headless = True
driver = webdriver.Chrome(chrome_options=option)
start_page = 'https://www.instagram.com/p/CYnKN53pgql/'
driver.get(start_page)

all_links = []
time.sleep(15)
for _ in range(10):
    try:
        necessary_link2 = driver.find_element(By.CSS_SELECTOR, 'img').get_attribute('src')
        all_links.append(necessary_link2)
        print(necessary_link2)
        next_page = driver.find_element(By.CSS_SELECTOR, 'button[class*="  _6CZji   "]')
        driver.execute_script("arguments[0].click();", next_page)

    except:
        print('all done')

def wget_download():
    directory = 'F:\Test2'
    for url in all_links:
        wget.download(url, out=directory)

if __name__ == '__main__':
    wget_download()
#solitude.aeternum
#23A8nDIVDh@#