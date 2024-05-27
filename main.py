import os
import requests
import json

from botasaurus.browser import broswer, Driver
from dotenv import load_dotenv
from flask import Flask, request, render_template
from models.huggingface_base import analyze_sentiment

app = Flask(__name__)

@app.route('/')
def home():
    return render_template(__name__, template_folder='index.html')

@broswer
def scrape_reviews(url, driver: Driver, data):
    driver.get(url)
    content = driver.get_text('faceplate-screen-reader-content')
    return {
        "content": content
    }

# @app.route('/scrape', methods=['POST'])
# def scrape():
#     url = request.form['url']
#     reviews = scrape_reviews(url)
#     sentiments = analyze_sentiment(reviews)
#     return render_template('results.html', reviews=reviews, sentiments=sentiments)

# def scrape_reviews(url):
#     # Load the API key
#     API_KEY = os.getenv('API_KEY')
#     client = ApifyClient(API_KEY)

#     # Prepare the Actor input
#     run_input = {
#         "startUrls": [{ "url": url }],
#         "maxReviews": 100,
#         "language": "en",
#     }
#     run = client.actor("compass/google-maps-reviews-scraper").call(run_input=run_input)
#     print("💾 Check your data here: https://console.apify.com/storage/datasets/" + run["defaultDatasetId"])
    
#     # Fetch data
#     dataset_items = client.dataset(run['defaultDatasetId']).list_items().items

#     # Extract reviews
#     reviews = [item['review'] for item in dataset_items]
    
#     # API_URL = f'https://api.scrapingdog.com/scrape?api_key={API_KEY}&url={url}&render_js=true'
#     # payload = {"startUrls": [{"url": url}]}

#     # Send a POST request to the API
#     # response = requests.post(API_URL, json=payload)
#     # if response.status_code == 200:
#     #     reviews = response.json()
#     #     return [review["text"] for review in reviews if "text" in review]
#     # else:
#     #     return []

if __name__ == '__main__':
    load_dotenv()
    app.run(debug=True)