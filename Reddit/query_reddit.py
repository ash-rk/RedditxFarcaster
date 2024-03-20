from reddit_auth import authenticate_reddit
import pandas as pd

def get_popular_subreddits(limit=50):
    reddit = authenticate_reddit()
    popular_subreddits = reddit.subreddits.popular(limit=limit)

    # Create a list of dictionaries for each subreddit
    subreddits_data = [{
        "Subreddit": subreddit.display_name, 
        "Subscribers": subreddit.subscribers
    } for subreddit in popular_subreddits]

    # Convert the list of dictionaries to a Pandas DataFrame
    df = pd.DataFrame(subreddits_data)

    # Sort the DataFrame by the 'Subscribers' column in descending order
    df_sorted = df.sort_values(by='Subscribers', ascending=False)
    df_sorted = df_sorted.reset_index(drop=True) # Reset index
    # Print the sorted DataFrame
    print(f"Trending channels: \n{df_sorted}")
    return df_sorted

def main():
    get_popular_subreddits(10)

if __name__ == "__main__":
    main()
