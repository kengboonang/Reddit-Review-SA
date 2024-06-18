import dotenv
import os
import praw

dotenv.load_dotenv()

class reddit:
    def __init__(self):
        self.reddit = praw.Reddit(
            client_id=os.environ.get("REDDIT_ID"),
            client_secret=os.environ.get("REDDIT_SECRET"),
            user_agent=os.environ.get("REDDIT_USER"),
            password=os.environ.get("REDDIT_PASS"),
        )

    def get_top_posts(self, subreddit, top_n, sort_by):
        """
        Get the top n posts from a subreddit
        """
        posts = []
        if sort_by == "Hot":
            for submission in self.reddit.subreddit(subreddit).hot(limit=top_n):
                posts.append(submission.selftext)
        elif sort_by == "Top":
            for submission in self.reddit.subreddit(subreddit).top(limit=top_n):
                posts.append(submission.selftext)
        elif sort_by == "New":
            for submission in self.reddit.subreddit(subreddit).new(limit=top_n):
                posts.append(submission.selftext)
        elif sort_by == "Rising":
            for submission in self.reddit.subreddit(subreddit).rising(limit=top_n):
                posts.append(submission.selftext)
    
        return posts
    
if __name__ == "__main__":
    print(reddit.read_only)

    # Get the top 10 hot posts from the subreddit 'test'
    for submission in reddit.subreddit('test').hot(limit=10):
        print(submission.title)