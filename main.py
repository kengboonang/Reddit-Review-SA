import os
import requests
import json

from dotenv import load_dotenv
from flask import Flask, request, render_template
from models.huggingface_base import analyze_sentiment

app = Flask(__name__)

@app.route('/')
def home():
    return render_template(__name__, template_folder='index.html')

# scraping code

if __name__ == '__main__':
    load_dotenv()
    app.run(debug=True)