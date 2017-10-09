import tweepy
from tweepy import OAuthHandler
import json

#informacoes de autenticacao
consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''

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
