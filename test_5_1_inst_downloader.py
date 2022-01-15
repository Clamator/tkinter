import tkinter as tk
from tkinter import  ttk
import time

import wget
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def wget_download(urls):
    directory = 'F:\Test2'
    for url in urls:
        wget.download(url, out=directory)


def get_link(queue=None):
    tk.Label(win, text='search begun').place(x=210, y=320, width=120, height=20)
    ttk.Progressbar(length=300, orient=tk.HORIZONTAL).place(x=310, y=300, width=120, height=20)
    option = Options()
    option.add_argument("--disable-blink-features=AutomationControlled")
    option.headless = True
    driver = webdriver.Chrome(chrome_options=option)
    start_page = link.get()
    driver.get(start_page)

    all_links = []
    for _ in range(121):
        try:
            necessary_link2 = driver.find_element(By.CSS_SELECTOR, 'img').get_attribute('src')
            all_links.append(necessary_link2)
            print(necessary_link2)
            next_page = driver.find_element(By.CSS_SELECTOR, 'button[class*="  _6CZji   "]')
            driver.execute_script("arguments[0].click();", next_page)
            tk.Label(win, text=f'{necessary_link2}').place(x=310, y=320, width=320, height=20)
        except:
            tk.Label(win, text='all done').place(x=310, y=320, width=320, height=20)

        wget_download(all_links)


win = tk.Tk()
win.title('test')
win.geometry('750x400+300+200')

tk.Label(win, text='ссылка на файл').place(x=10, y=10, width=120, height=20)


link = tk.Entry(win)
salary = tk.Entry(win)

link.place(x=130, y=10, width=500, height=20)


tk.Button(win, text='Поиск!', command=get_link).place(x=310, y=350, width=120, height=20)

if __name__ == '__main__':
    win.mainloop()