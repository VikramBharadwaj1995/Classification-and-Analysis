# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 20:18:57 2017

@author: Vikram Bharadwaj
"""
# This is a Simple Aplication that classifies a Tweet as a Positive one or a Negative one.

import tweepy
from textblob import TextBlob

consumerKey = #Enter your key
consumerKeySecret = #Enter your key

accessToken = #Enter your key
accessTokenSecret = #Enter your key

loginAuth = tweepy.OAuthHandler(consumerKey, consumerKeySecret)
loginAuth.set_access_token(accessToken, accessTokenSecret)

TwitterApi = tweepy.API(loginAuth)

print("Enter a particular Search Term/Query, to get an Analysis on the Polarity and Subjectivity of a tweet with that term!")
inputQuery = input()
publicTweets = TwitterApi.search(inputQuery)

for tweet in publicTweets:
    print(tweet.text)
    textTweet = tweet.text
    tweetAanalysis = TextBlob(textTweet)
    print(tweetAanalysis.sentiment)
    print("\n")
    
