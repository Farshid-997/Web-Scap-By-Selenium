from bs4 import BeautifulSoup
from selenium import webdriver
import time
import csv
import pandas as pd
from csv import writer


file_name = 'Sample_Data.csv'

column_headings = [
    'CO2 Emission Saved (ton)', 'Equivalent Trees Plant (trees)', 'Total Income ($)']
with open(file_name, 'a+', newline='') as write_obj:
    csv_writer = writer(write_obj)
    csv_writer.writerow(column_headings)


def append_list_as_row(file_name, list_of_elem):
    with open(file_name, 'a+', newline='') as write_obj:
        csv_writer = writer(write_obj)
        csv_writer.writerow(list_of_elem)


option = webdriver.ChromeOptions()

option.add_argument('--no-sandbox')
option.add_argument('--disable-dev-sh-usage')

driver = webdriver.Chrome(
    'C:\Program Files (x86)\WebDriver\chromedriver', options=option)


driver.get('https://fop.saj-electric.com/bigScreen/rollSinglePlant?viewKey=363e6363922508f0adb17ecc889b2def1d7e3265472a6ab9fda0a682a0fa9fc7f5d7d20c5c8389c4b2ba38cb3fd9908f8ea64a9c4ec7cb3264a052519ea3a274e4277fe376c2b2a44e24490e53785083eb9077c945b217d991eb6df0b13fa74b&start=3&lang=en')
time.sleep(20)
while(True):
    time.sleep(5)
    url = driver.current_url

    driver.get(url)

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    links = soup.select(".cumulate li")

    global_list = []
    for i in links:
        data = str(i.text).split('\n')
        data_value = data[1]
        global_list.append(data_value)

    append_list_as_row(file_name, global_list)
