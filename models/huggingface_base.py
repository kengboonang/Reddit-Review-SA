from transformers import pipeline

sentiment_pipeline = pipeline(task="sentiment-analysis")

def prepare_reviews(data):
    reviews = []
    for review in data:
        reviews.append(review.text)
    return reviews

def analyze_sentiment(reviews):
    sentiments = []
    for review in reviews:
        result = sentiment_pipeline(review)[0]
        sentiments.append(result)
    return sentiments