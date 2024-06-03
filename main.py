import os
import requests
import json

from dotenv import load_dotenv
from flask import Flask, request, render_template
from models.huggingface_base import analyze_sentiment, prepare_reviews
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 
from webdriver_manager.chrome import ChromeDriverManager

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", template_folder='templates')

# scraping code
@app.route('/scrape', methods=['POST'])
def scrape():
    # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    url = request.form['url']
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url)
    # ensure that url is from reddit
    # try:
    #     assert "reddit" in driver.title
    # except AssertionError:
    #     raise( AssertionError("Please enter a valid Reddit URL"))
    
    # Scroll down to load more content
    for _ in range(10):
        driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
        time.sleep(2)
    
    elements = driver.find_elements(By.CSS_SELECTOR, "div[data-post-click-location='text-body'] p")
    reviews = prepare_reviews(elements)
    sentiments = analyze_sentiment(reviews)
    pos_count = len([1 for sentiment in sentiments if sentiment["label"] == 'POSITIVE'])
    neg_count = len([1 for sentiment in sentiments if sentiment["label"] == 'NEGATIVE'])
    return render_template('results.html', reviews=zip(reviews, sentiments), pos_count=pos_count, neg_count=neg_count, template_folder='templates')

if __name__ == '__main__':
    load_dotenv()
    app.run(debug=True)