#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import tweepy, time, sys
from random import randint
from time import sleep
 
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

for tweet in tweepy.Cursor(api.search, q ='Garfield', lang = 'en').items():
	rand_quote_index = randint(0, 25)
	quote = q_f[rand_quote_index]
	
	try:
		print(tweet.created_at)
		# api.update_status(status=quote)
		# sleep(100)
	except tweepy.TweepError as e:
		print(e.reason)
		sleep(100)
		continue
	except StopIteration:
		break