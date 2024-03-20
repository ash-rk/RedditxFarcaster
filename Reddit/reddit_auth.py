from dotenv import load_dotenv
import os
import praw

def authenticate_reddit():
    # Load environment variables from .secrets file
    load_dotenv('.secrets')

    # Access secrets
    client_id = os.getenv('REDDIT_CLIENT_ID')
    client_secret = os.getenv('REDDIT_CLIENT_SECRET')
    user_agent = os.getenv('REDDIT_USER_AGENT')

    # Authenticate and access Reddit API
    reddit = praw.Reddit(
        client_id=client_id,
        client_secret=client_secret,
        user_agent=user_agent
    )

    return reddit
