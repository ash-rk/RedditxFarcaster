# Farcaster vs Reddit Engagement Analysis

## Overview

This project aims to dissect and analyze the intricacies of user engagement across two distinct social platforms: Farcaster and Reddit, a well-established community-driven forum. By extracting and comparing data from Reddit's API and Dune Analytics (focusing on Farcaster), we delve into the dynamics of user interaction, content popularity, and the overall growth trajectory of these platforms.

## Data Collection

- **Reddit**: Utilized the Reddit API to fetch detailed metrics surrounding subreddit engagement, including post interactions and overall community engagement stats.
- **Farcaster**: Executed targeted queries via Dune Analytics, focusing on extracting expansive datasets related to Farcaster's channel activities and user engagement metrics.

## Data Preparation and Analysis

A multi-faceted approach was adopted for data preparation, ensuring a robust foundation for the ensuing analysis. Key steps included:

- **Data Cleansing**:
  - Extracting and refining channel and subreddit names from embedded HTML tags.
  - Standardizing column names across datasets to maintain consistency.

- **Data Enrichment**:
  - Deriving key engagement metrics, including ratios and growth indices.
  - Aggregating statistics to capture overall and average engagement insights.

- **Data Merging**:
  - Integrating Farcaster and Reddit data on comparable metrics (e.g., channels vs. subreddits) to facilitate a direct comparative analysis while maintaining data integrity.

### Jupyter Notebook Analysis

Interactive Python scripting via Jupyter Notebooks was leveraged to:

- **Identify Engagement Trends**: Isolating highly active communities by scrutinizing engagement trends over selected periods.
- **Highlight Growth Dynamics**: Ranking Farcaster channels by growth, considering channel age and activity metrics.
- **Draw Comparative Insights**: Directly contrasting Farcaster channels against Reddit subreddits to uncover unique patterns and behaviors.

## Technologies

- **Python**: For comprehensive data manipulation and analysis.
  - **Key Libraries**: `pandas` for data analysis, `matplotlib` for visualization, `PRAW` for fetching Reddit data.
- **Dune Analytics**: Accessed for Farcaster data insights.
- **Jupyter Notebook**: Utilized for conducting and documenting the analysis process.

## Getting Started

### Prerequisites

- Python 3.8 or later
- Jupyter Notebook or JupyterLab

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/ash-rk/RedditxFarcaster.git

2. Install python packages:
pip install pandas praw matplotlib

3. Setup credentials in .secret file
REDDIT_CLIENT_ID='your_client_id'
REDDIT_CLIENT_SECRET='your_client_secret'
DUNE_API_KEY='your_dune_api_key'  # If applicable

### Steps to Run

Follow these steps to execute the analysis:

1. **Reddit Data Extraction**
   - Navigate to the `Reddit` folder and run the script for extracting Reddit data.
     ```sh
     python3 analyze_subreddits.py
     ```

2. **Farcaster Data Extraction**
   - Move to the `Farcaster` folder and execute the script to gather Farcaster channel and user metrics.
     ```sh
     python3 fc_channel_query.py
     ```

3. **Data Cleaning**
   - Still within the `Farcaster` folder, run the following script to clean the gathered Farcaster data.
     ```sh
     python3 dune_result_analysis.py
     ```
3. **Farcaster Follower data**
   - Still within the `Farcaster` folder, run the following script to clean the gathered Farcaster data.
     ```sh
     python3 scrape.py
     ```

5. **Analysis Notebook**
   - Open the `Farcaster vs Reddit Analysis.ipynb` notebook located in the main directory and run all cells to perform the analysis.

Note: The output files generated from steps 1 to 3 are stored in the `data_retrieved` folder for easy access.


## License
This project is licensed under the MIT License