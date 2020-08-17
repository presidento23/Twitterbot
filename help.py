from Exclude import API_Info
import tweepy

auth = tweepy.OAuthHandler(API_Info.api_key,API_Info.secret_api_key)
auth.set_access_token(API_Info.access_token,API_Info.secret_acess_token)
