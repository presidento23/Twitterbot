import logging
import os

import tweepy

logger = logging.getLogger()

os.environ['api_key'] = ""
os.environ['secret_api_key'] = ""
os.environ['access_token'] = ""
os.environ['secret_access_token'] = ""

def CreateApi():
    auth = tweepy.OAuthHandler(os.getenv('api_key'),os.getenv('secret_api_key'))
    auth.set_access_token(os.getenv('access_token'),os.getenv('secret_access_token'))

    api = tweepy.API(auth,wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    try:
        api.verify_credentials()

    except Exception as e:
        logger.error(f"Error creating API \n {e}",exc_info = True)
        raise e

    logger.info("API Created")
    return api

