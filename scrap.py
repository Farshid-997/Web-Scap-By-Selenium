from bs4 import BeautifulSoup
from selenium import webdriver
import time
option = webdriver.ChromeOptions()
# I use the following options as my machine is a window subsystem linux.
# I recommend to use the headless option at least, out of the 3
option.add_argument('--headless')
option.add_argument('--no-sandbox')
option.add_argument('--disable-dev-sh-usage')
# Replace YOUR-PATH-TO-CHROMEDRIVER with your chromedriver location
driver = webdriver.Chrome(
    'C:\Program Files (x86)\WebDriver\chromedriver', options=option)

# Getting page HTML through request
time.sleep(0.4)
while(True):

    driver.get('https://fop.saj-electric.com/bigScreen/rollSinglePlant?viewKey=363e6363922508f0adb17ecc889b2def1d7e3265472a6ab9fda0a682a0fa9fc7f5d7d20c5c8389c4b2ba38cb3fd9908f8ea64a9c4ec7cb3264a052519ea3a274e4277fe376c2b2a44e24490e53785083eb9077c945b217d991eb6df0b13fa74b&start=3&lang=en')
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    links = soup.select(".cumulate li")

    for i in links:
        print(i.text)
        print("execution")
