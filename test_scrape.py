from twikit import Client, TooManyRequests

import time
from datetime import datetime
import csv
from configparser import ConfigParser
from random import randint

client = Client(language='en-US')

Query = 'Appl stock'
client.load_cookies("cokkies.json")
async def get_tweets(client, Query):
    tweets = client.search_tweet(Query)
    for tweet in tweets:
        print(vars(tweet))
        

async def main():
    await get_tweets(client, Query)
