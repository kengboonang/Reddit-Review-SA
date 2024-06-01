import os
import requests
import json

from dotenv import load_dotenv
from flask import Flask, request, render_template
from models.huggingface_base import analyze_sentiment
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 
from webdriver_manager.chrome import ChromeDriverManager

app = Flask(__name__)

@app.route('/')
def home():
    return render_template(__name__, template_folder='index.html')

# scraping code
@app.route('/scrape', methods=['POST'])
def scrape():
    # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    url = request.form['url']
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url)
    # ensure that url is from reddit
    try:
        assert "reddit" in driver.title
    except AssertionError:
        raise( AssertionError("Please enter a valid Reddit URL"))
    
    # Scroll down to load more content
    for _ in range(10):
        driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
        time.sleep(2)
    
    elements = driver.find_elements(By.CSS_SELECTOR, "div[data-post-click-location='text-body'] p")
    return elements

if __name__ == '__main__':
    load_dotenv()
    app.run(debug=True)