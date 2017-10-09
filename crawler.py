import tweepy
from tweepy import OAuthHandler
import json

#informacoes de autenticacao
consumer_key = '7lwZXig2oVGkAMncLjGuGKcx1'
consumer_secret = 'DhK5yjrUy8yAncaiMT2KjqMBdWd8hIJ6OMBgsgyBPc71ElyJXO'
access_token = '917082052306096128-S3PaxP37XCPASLLa8G3MdGl9BchEisu'
access_secret = '8SyLjbMhhI5MCrDyYgdPA0RtV7HpNP3ZvyvHNzscMsk7s'

def get_tweets(user):
	contador = 0

	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_secret)
 
	api = tweepy.API(auth)
	tweets = []

	for tweet in tweepy.Cursor(api.user_timeline, id=user).items():
		tweets.append(tweet._json)
		contador += 1
		print(contador)
	
	with open(user +".json", "w") as outfile:
		json.dump(tweets, outfile, indent=1)


if __name__ == '__main__':
	get_tweets('LeiSecaRJ')