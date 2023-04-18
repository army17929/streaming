import pandas as pd 
import numpy as np 
import tweepy as tp
# In this script, we are going to stream tweets into the script. 
# This script is motivated by event-driven programming.
# The streamed tweets will be tallied in the csv.file. 

# For the authentication, we need the keys for using this API
twitter_app_key = '5hNJkw7VVVHGN3T44R58TajMn'
twitter_app_secret = 'ynT8mrriAO3Nqnkn7hxCmh2VRMgRSPqRNDxk51593MtL2orzoJ'
twitter_key = '1648376696415064064-Zx74uq8OFWXyjYZsNuqHYkpFlBJaZt'
twitter_secret = '1RJTGWSybgniIB9adf7GV9uCFbWMxJoNUC9JjzQ70efxR'
bearer_token='AAAAAAAAAAAAAAAAAAAAAApGmwEAAAAAOcxv%2Fl8DJpMr99gn5EfBWiS1rgw%3DanbHvgBB6jNGY3636MxFrMDAEnrWvL8RzMWxhsrBFJDsjeUGvb'

auth = tp.OAuthHandler(twitter_app_key,twitter_app_secret)
auth.set_access_token(twitter_key,twitter_secret)
api = tp.API(auth)
