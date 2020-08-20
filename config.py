import logging
import os

import tweepy

logger = logging.getLogger()

os.environ['api_key'] = "kW290anYbU4HTGayeoL9jIn5s"
os.environ['secret_api_key'] = "8dDchNDR3egYHsjrk6V9FKhwhH3fIDkzp0xkE3tvobOYChAno9"
os.environ['access_token'] = "1295144114812596225-WXm9wycAC2KQoHWdmUxy30wUREFU9V"
os.environ['secret_access_token'] = "bCERJHG5f0L8ddaFIzX6TE4NO1yZAxYlU1HQ8aRkySjo6"

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

