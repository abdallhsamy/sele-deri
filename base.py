#!/env/python3

from tarfile import NUL
from flask import (Flask, render_template)
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By;
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from markupsafe import escape


# define chrome driver path
DRIVER_PATH = '/usr/bin/chromedriver'

# @todo: update this before deploying
# DRIVER_PATH = './chromedriver'

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/deltas/<id>")
def getDelta(id):
    deltaId = escape(id)

    driver = webdriver.Chrome(DRIVER_PATH, options=chrome_options)
    driver.mobile
    driver.get('https://deri.io/#/trade/options/'+deltaId)

    try:
        sleep(1)
        items = driver.find_elements(By.CSS_SELECTOR, '.contract .c-body .c-row')
        
        # Delta object
        return items[10].text.split('\n')
        
    except:
        return ['delta', None]
    finally: 
        driver.quit()


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')