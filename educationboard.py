from selenium import webdriver
import pandas as pd
import time

# driver = webdriver.Chrome('chromedriver')
driver = webdriver.Chrome(
    'C:\Program Files (x86)\WebDriver\chromedriver')
driver.get('http://www.btebcbt.gov.bd/utility/instituteList?search=&max=100')

row_list_of_lists = []


def save_to_csv(row_list_of_lists):
    df = pd.DataFrame(row_list_of_lists, columns=[
                      'institute_code', 'institute_name', 'address', 'mobile_no', 'ein', 'email', 'division'])
    df.to_csv('X Bangladesh Technical Education Board.csv', index=None)


while True:
    row_data = driver.find_elements(
        "xpath", '//*[@id="list-competencyStandardUpload"]/div[2]/div/table/tbody/tr')
    for r in row_data:
        col_data = r.find_elements('xpath', 'td')

        institute_code = col_data[0].text
        institute_name = col_data[1].text
        address = col_data[2].text
        mobile_no = col_data[3].text
        ein = col_data[4].text
        email = col_data[5].text
        division = col_data[6].text

        row_list_of_lists.append(
            [institute_code, institute_name, address, mobile_no, ein, email, division])

    print(len(row_list_of_lists))

    try:
        next_button = driver.find_element("link text", "Next")
        next_button.click()
        print('Page clicked!')
        time.sleep(10)
    except:
        save_to_csv(row_list_of_lists)
        break
