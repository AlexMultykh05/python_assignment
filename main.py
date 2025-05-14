import tweepy
import configparser

# Read the configuration file
config = configparser.ConfigParser(interpolation=None) # To avoid issues with special characters
config.read('python_assignment/config.ini')

bearer_token = config['twitter']['bearer_token']
api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']
access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

# Create Tweepy Client for Twitter API v2
client = tweepy.Client(
    bearer_token=bearer_token,
    consumer_key=api_key,
    consumer_secret=api_key_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)

# Get my own user ID
user = client.get_me()
user_id = user.data.id
print(f"Authenticated as @{user.data.username} (ID: {user_id})")

# Fetch recent tweets/retweets from my timeline (includes retweets)
response = client.get_users_tweets(
    id=user_id,
    max_results=10,
    tweet_fields=['created_at', 'public_metrics'],
    expansions=['referenced_tweets.id']
)

# Print my tweets
print("\nMy latest tweets/retweets:")
if response.data:
    for tweet in response.data:
        print(f"- {tweet.created_at}: {tweet.text}")
else:
    print("No tweets found.")
