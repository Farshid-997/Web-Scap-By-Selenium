from selenium import webdriver
import pandas as pd
import time
import csv


driver = webdriver.Chrome(
    'C:\Program Files (x86)\WebDriver\chromedriver')


driver.get('https://www.eprocure.gov.bd/resources/common/StdTenderSearch.jsp?h=t')
time.sleep(2)

# Go to specific page number, if script fails due to network error.
page_number = '580'
text_box_field = driver.find_element("id", "dispPage")
text_box_field.clear()
text_box_field.send_keys(page_number)

# Click 'Go to Page' button
go_to_page_button = driver.find_element("id", "btnGoto")
go_to_page_button.click()
time.sleep(2)


def save_to_csv(data_lists):
    with open("output_e_tender1.csv", "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(data_lists)


while True:
    data_lists = []

    table = driver.find_element("xpath", '//*[@id="resultTable"]/tbody')
    row_data = table.find_elements("xpath", 'tr')

    for tr in row_data:
        col_data = tr.find_elements("xpath", 'td')
        if len(col_data) != 0:
            data_lists.append([col_data[0].text, col_data[1].text, col_data[2].text,
                              col_data[3].text, col_data[4].text, col_data[5].text])

    save_to_csv(data_lists)
    next_button = driver.find_element("link text", "Next")
    next_button.click()
    print('button clicked')
    time.sleep(2)
