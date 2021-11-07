from selenium import webdriver 
from bs4 import BeautifulSoup
import time 
import csv


START_URL = "https://en.wikipedia.org/wiki/List_of_solar_eclipses_in_the_21st_century"

browser = webdriver.Chrome("/Users/shenayaverma/Desktop/python/scraper/chromedriver.exe")

browser.get(START_URL) 

time.sleep(10)

def scrapedata():
    eclipse_data = []
    soup = BeautifulSoup(browser.page_source, "html.parser")
    for i in soup:
        k = i.find_all('th',attrs={"class", "nowrap"})
        print(k)

scrapedata()

    