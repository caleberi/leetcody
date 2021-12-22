from os import environ
from dotenv import load_dotenv
from requests import get

class Tweet:
    pass

BASE_URL = environ["TWITTER_URL_ENDPOINT"]

def build_tweet_stream_endpoint(**query):
    url = BASE_URL+"/sample/stream?"
    for k,v in query.items():
        url+="&"+f"{k}={v}"
    return url


def get_tweet(url,headers_={}):
    response = get(
        url,
        headers=headers_
    )
    for tweet in response.json():
        yield Tweet(tweet)

    