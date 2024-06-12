import dotenv
import os
import praw

dotenv.load_dotenv()

reddit = praw.Reddit(
    client_id=os.environ.get("REDDIT_ID"),
    client_secret=os.environ.get("REDDIT_SECRET"),
    user_agent=os.environ.get("REDDIT_USER"),
    password=os.environ.get("REDDIT_PASS"),
)

print(reddit.read_only)

# Get the top 10 hot posts from the subreddit 'test'
for submission in reddit.subreddit('test').hot(limit=10):
    print(submission.title)