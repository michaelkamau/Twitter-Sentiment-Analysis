import tweepy
import json
from twitter_sentiment_analysis import authentication

# TODO: Wrap this in function -- init_api()
api = authentication.authenticate()

tweets_list = []


def get_last_200_tweets():
    """
    Gets the latest 200 tweets if available, add them to tweet_list
    """
    for status in tweepy.Cursor(api.user_timeline).items(2):
        tweets_list.append(status._json)


def save_tweets_json_file():
    """
    Save the collected tweets onto a JSON file
    """
    with open('allTweets.json', 'w') as f:
        json.dump(tweets_list, f)


def load_tweets_json_file():
    """
    Load the JSON file with tweets, decode the data to Python types
    """
    with open('allTweets.json', 'r') as f:
        tweets_list = json.load(f)
