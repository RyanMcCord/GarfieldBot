#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import tweepy, time, sys
from random import randint
from time import sleep

# custom filters on tweets to choose what tweets to respond to
def checkForReply(status):
	if (status.is_quote_status):
		return False
	if hasattr(status, 'retweeted_status'):
		return False
	if 'andrew garfield' in status.text.lower():
		return False
	if 'andrewgarfield' in status.text.lower():
		return False
	if 'garfield park' in status.text.lower():
		return False
	if 'garfield rd' in status.text.lower():
		return False
	if 'james garfield' in status.text.lower():
		return False
	if 'james a' in status.text.lower():
		return False
	if 'garfield st' in status.text.lower():
		return False
	if 'garfield street' in status.text.lower():
		return False
	return True

# custom listener that builds from the tweepy listener, allowing the Garfield Bot to reply
class MyStreamListener(tweepy.StreamListener):
	def on_status(self, status):
		# print(status.text.encode("utf-8"))
		# print(status.user.screen_name)
		should_bot_reply = checkForReply(status)
		if (should_bot_reply):
			rand_quote_index = randint(0, 25)
			quote = q_f[rand_quote_index]
			sn = status.user.screen_name
			message = "@%s " % (sn)
			message += quote
			while (len(message) > 140):
				rand_quote_index = randint(0, 25)
				quote = q_f[rand_quote_index]
				sn = status.user.screen_name
				message = "@%s " % (sn)
				message += quote
			api.update_status(message, status.id)
			sleep(86)


# get the info from our two files
quote_file = str(sys.argv[1])
keys_file = str(sys.argv[2])

# this code block gets the random quotes
quote_file_name = open(quote_file,'r')
q_f = quote_file_name.readlines()
quote_file_name.close()

# this code block gets our authorization keys
key_file_name = open(keys_file,'r')
k_f = key_file_name.readlines()
key_file_name.close()

# keys are retrieved from our file
CONSUMER_KEY = k_f[0].replace('\n', '')
CONSUMER_SECRET = k_f[1].replace('\n', '')
ACCESS_KEY = k_f[2].replace('\n', '')
ACCESS_SECRET = k_f[3].replace('\n', '')

# authorize the bot
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

# stream tweets in real time to reply to people who tweet about garfield
myStreamListener = MyStreamListener
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener())
myStream.filter(languages=['en'], track=['Garfield'])