import streamlit as st

from models.saved_model import model, tokenizer, predict_sentiment
from utils.BERT_processing import tokenize_function
from utils.reddit_processing import reddit


# Streamlit page that takes in a user input which is the name of a reddit subreddit
# User can decide the top number of posts to display
# Page will perform sentiment analysis on the posts in the subreddit page

st.title("Reddit Sentiment Analysis")

subreddit = st.text_input("Enter the name of a subreddit")
top_n = st.slider("Select the number of top posts to display", 1, 200, 5)
sort_by = st.selectbox("Sort by", ["Hot", "Top", "New", "Rising"])

if subreddit:
    st.write(f"Displaying top {top_n} posts from r/{subreddit}")

    reddit_obj = reddit()
    posts = reddit_obj.get_top_posts(subreddit.lower(), top_n, sort_by)

    # st.write(posts[:2])

    # buffer icon while processing
    with st.spinner("Retrieving posts..."):
        encodings = [tokenize_function(post, tokenizer) for post in posts]
    with st.spinner("Analyzing sentiment..."):
        sentiments = [predict_sentiment(encoding, model) for encoding in encodings]
        pos_count = len([1 for sentiment in sentiments if sentiment == 'positive'])
        neg_count = len([1 for sentiment in sentiments if sentiment == 'negative'])

        # st.write(sentiments[:2])
        # display bar chart of sentiment distribution with label
        st.title("Sentiment Distribution")
        st.bar_chart({"Positive": pos_count, "Negative": neg_count})

        sentiment_dict = zip(posts, sentiments)
        st.title("Posts and Sentiments")
        for post, sentiment in sentiment_dict:
            st.write(f"Post content: \n{post}")
            st.write(f"Sentiment: \n{sentiment}")
            st.write("----")