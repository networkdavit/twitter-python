import tweepy
from time import sleep
import os.path
import pyfiglet

welcome = pyfiglet.figlet_format("AUTO TWEET")
print(welcome)
  
consumer_key = "zWHkZyvXfMXGMZfhfTCDMFgaa" #please enter your consumer key here
consumer_secret = "LUAt19qFGJCMpXfRE40yrWSuCfoJnv3BcHRmHkp5P8qoAEM6g4" #please enter your consumer secret here
access_token = "1392399035223453701-AUvoEjKdusJiFlqIPX3DRDitKWtuvu" #please enter your access token here
access_token_secret = "faYQoBHEaZSrN4SGfTTvjS2eL3JAuR8WnMrPsJxyH2D2T" #please enter your access token secret here
  
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
   
auth.set_access_token(access_token, access_token_secret)
  
api = tweepy.API(auth)

run = True

while run:
	file_location = input("Please enter the file location:")
	if os.path.isfile(file_location):
	    run = False
	else:
		print("File doesn't exist")


delay = int(input("Please enter how long should you wait before the next tweet in minutes?:"))
 
file = open(file_location, "r")
list_of_tweets = file.readlines()

for tweet in list_of_tweets: 
	if tweet != list_of_tweets[-1]:
		api.update_status(tweet)
		sleep(delay*60)
	else:
		api.update_status(list_of_tweets[-1])
