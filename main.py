import os
import requests
import json

from dotenv import load_dotenv
from flask import Flask, request, render_template
from models.huggingface_base import analyze_sentiment

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    url = request.form['url']
    reviews = scrape_reviews(url)
    sentiments = analyze_sentiment(reviews)
    return render_template('results.html', reviews=reviews, sentiments=sentiments)

def scrape_reviews(url):
    # Load the API key
    API_KEY = os.getenv('API_KEY')
    API_URL = f'https://api.scrapingdog.com/scrape?api_key={API_KEY}&url={url}&render_js=true'
    payload = {"startUrls": [{"url": url}]}

    # Send a POST request to the API
    response = requests.post(API_URL, json=payload)
    if response.status_code == 200:
        reviews = response.json()
        return [review["text"] for review in reviews if "text" in review]
    else:
        return []

if __name__ == '__main__':
    load_dotenv()
    app.run(debug=True)