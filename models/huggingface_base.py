from transformers import pipeline

sentiment_pipeline = pipeline("sentiment-analysis")

def analyze_sentiment(reviews):
    sentiments = []
    for review in reviews:
        result = sentiment_pipeline(review)[0]
        sentiments.append(result)
    return sentiments