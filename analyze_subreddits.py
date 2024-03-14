# analyze_subreddits.py
from reddit_auth import authenticate_reddit
import pandas as pd

# Attempt to import get_popular_subreddits; if not available, set a flag
try:
    from query_reddit import get_popular_subreddits
    can_fetch_popular = True
except ImportError:
    can_fetch_popular = False

def get_post_metrics(subreddit_name, time_filter='week', limit=10):
    reddit = authenticate_reddit()
    subreddit = reddit.subreddit(subreddit_name)
    top_posts = subreddit.top(time_filter=time_filter, limit=limit)
    
    total_comments = 0
    total_score = 0
    total_upvote_ratio = 0
    total_awards = 0
    posts_counted = 0
    
    for post in top_posts:
        total_comments += post.num_comments
        total_score += post.score
        total_upvote_ratio += post.upvote_ratio
        total_awards += sum(award['count'] for award in post.all_awardings)
        posts_counted += 1
    
    avg_comments = total_comments / posts_counted if posts_counted else 0
    avg_score = total_score / posts_counted if posts_counted else 0
    avg_upvote_ratio = total_upvote_ratio / posts_counted if posts_counted else 0
    avg_awards = total_awards / posts_counted if posts_counted else 0
    
    return avg_comments, avg_score, avg_upvote_ratio, avg_awards, posts_counted

def analyze_subreddits(subreddits=None, time_filter='week', limit=10):
    # If no custom list provided and fetching top subreddits is possible
    if subreddits is None and can_fetch_popular:
        subreddits_df = get_popular_subreddits(limit)
        subreddits = subreddits_df['Subreddit'].tolist()
    
    analysis_results = []
    
    for subreddit_name in subreddits:
        avg_comments, avg_score, avg_upvote_ratio, avg_awards, avg_posts = get_post_metrics(subreddit_name, time_filter, limit)
        analysis_results.append({
            "Subreddit": subreddit_name,
            "Average Comments": avg_comments,
            "Average Score": avg_score,
            "Average Upvote Ratio": avg_upvote_ratio,
            "Average Awards": avg_awards,
            "Posts Counted": avg_posts
        })
        
    analysis_df = pd.DataFrame(analysis_results)
    print(f"\nSubreddit insights based on the top {limit} posts of the last {time_filter}:\n{analysis_df}")

if __name__ == "__main__":
    # To specify subreddits, do it here, otherwise leave it as None to auto fetch top subreddits
    custom_subreddits = None  # Example: ['ai', 'MachineLearning', 'datascience']
    analyze_subreddits(custom_subreddits, time_filter='week', limit=10)
