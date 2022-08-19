#!/env/python

from flask import Flask

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By;
from selenium.webdriver.chrome.options import Options
from markupsafe import escape


# define chrome driver path
DRIVER_PATH = '/usr/bin/chromedriver'
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

app = Flask(__name__)
@app.route("/deltas/<id>")
def hello_world(id):
    deltaId = escape(id)
    try:
        driver = webdriver.Chrome(DRIVER_PATH, options=chrome_options)

        driver.get('https://deri.io/#/trade/options/'+deltaId)

        # sleep until page fully loades
        sleep(1)

        # Get contact items
        items = driver.find_element(By.CLASS_NAME, 'contract')
        
        # Get c-row
        orders = items.find_elements(By.CLASS_NAME, 'c-row')

        # Delta object
        print(orders[10].text.split('\n'))
        return orders[10].text.split('\n')
        
    finally:
        driver.quit()

