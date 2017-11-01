


# sentiment analysis


import tweepy 
from textblob import TextBlob



cs_key = "5KyrGM2OqrccbzWmPdZ3kt8x21"
cs_secret  = "Of5JNOoEX05kxIQUtJra2DmJkU5zY2Ma9PAio8NUQ3a8KMcA79"

acs_token = "135848361-gKCJQfkFyjZX3w5xWdeIRQd4srzu31acUXc4t829"
acs_secret = "k88xBImk9ALyLPs1h6I3Zi2dglZRN6ARPpWFxGlFsZyMG"

auth = tweepy.OAuthHandler(cs_key,cs_secret)

auth.set_access_token(acs_token,acs_secret)

api = tweepy.API(auth)





public_tweet = api.search('StrangerThings2')

for tweet in public_tweet:
    #print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
      
 