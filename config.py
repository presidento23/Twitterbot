import logging
import os

import tweepy

logger = logging.getLogger()

def create_api():
    auth = tweepy.OAuthHandler(os.getenv('api_key'),os.getenv('secret_api_key'))
    auth.set_access_token(os.getenv('access_token'),os.getenv('secret_acess_token'))

    api = tweepy.API(auth,wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    try:
        api.verify_credentials()
        print("Authenticated Ok")

    except Exception as e:
        logger.error("Error creating API", exc_info = True)
        raise e

    logger.info("API Created")
    return api