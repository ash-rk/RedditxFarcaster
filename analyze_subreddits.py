from reddit_auth import authenticate_reddit
import pandas as pd

# Attempt to import get_popular_subreddits; if not available, set a flag
try:
    from query_reddit import get_popular_subreddits
    can_fetch_popular = True
except ImportError:
    can_fetch_popular = False

def get_post_metrics(subreddit_name, time_filter='week', limit=500):
    reddit = authenticate_reddit()
    subreddit = reddit.subreddit(subreddit_name)
    # Retrieve the subreddit's subscriber count
    subscriber_count = subreddit.subscribers
    
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
    
    # Include subscriber_count in the return statement
    return total_comments, total_score, total_upvote_ratio, total_awards, posts_counted, subscriber_count

def analyze_subreddits(subreddits=None, time_filter='week', limit=500):
    if subreddits is None and can_fetch_popular:
        subreddits_df = get_popular_subreddits(limit)
        subreddits = subreddits_df['Subreddit'].tolist()
    
    analysis_results = []
    
    for subreddit_name in subreddits:
        total_comments, total_score, total_upvote_ratio, total_awards, total_posts, subscriber_count = get_post_metrics(subreddit_name, time_filter, limit)
        analysis_results.append({
            "Subreddit": subreddit_name,
            "Subscribers": subscriber_count,  # Add subscriber count to results
            "Total Comments": total_comments,
            "Total Score": total_score,
            "Total Upvote Ratio": total_upvote_ratio / total_posts if total_posts > 0 else 0,
            "Total Awards": total_awards,
            "Posts Counted": total_posts
        })
        
    analysis_df = pd.DataFrame(analysis_results)
    # Output the DataFrame to a CSV file
    csv_filename = f"subreddit_insights_{time_filter}.csv"
    analysis_df.to_csv(csv_filename, index=False)
    print(f"Subreddit insights based on the top {limit} posts of the last {time_filter} have been saved to {csv_filename}")

if __name__ == "__main__":
    custom_subreddits = None  # Adjust this list for custom analysis
    analyze_subreddits(custom_subreddits, time_filter='week', limit=500)
