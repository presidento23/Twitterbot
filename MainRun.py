import logging
import tweepy

from config import CreateApi
import json

logging.basicConfig(level = logging.INFO)
logger = logging.getLogger()

class Day_Trade_Listener():
    def __init__(self,api, who:str):
        self.api = api
        self.me = api.me()

    def MostRetweetHighestScoredTweet(self):
        Totalweight = {}


        try:
            Last30tweets = (self.api.user_timeline(self.who, count=30))
            logger.info("30 tweets found")
        except Exception as e:
            logger.error("Error finding 30 tweets", exc_info=True)
            return
        for tweet in Last30tweets:
            Tweetretweets = tweet.retweet_count
            Tweetfavorites = tweet.favorite_count
            Weightedretweetsscore = (Tweetretweets - 0) / (50)
            WeightedFavoritescore = (Tweetfavorites - 0) / (70)
            Temptotal = Weightedretweetsscore + WeightedFavoritescore
            if Temptotal >= 0.7:
                try:
                    self.api.retweet(tweet.id)
                    logger.info(f"Retweeted {tweet.id} witih score of {Temptotal}")
                except Exception as e:
                    logger.error(f"Error retweeting {tweet.id}.")
                return
            else:
                Totalweight[Temptotal] = tweet.id
        Highestscore = max(Totalweight)
        Highestscoreid = Totalweight[Highestscore]
        try:
            print(Highestscoreid)
            self.api.retweet(Highestscoreid)
            logger.info(f"Retweeted {Highestscoreid} witih score of {Highestscore}")
        except Exception as e:
            logger.error(f"Error retweeting {tweet.id}.")
        return

    def GainAttention(self):

        try:
            Targetuserid = self.api.get_user(self.who)
            logger.info(f"Found user {self.who}")

        except Exception as e:
            logger.error(f"Error locating usering in function GainAttention")
            return

        try:

            for follower in tweepy.Cursor(self.api.followers, id = Targetuserid).items():


def main():
    api = CreateApi()
    Bot = Day_Trade_Listener(api, who = "WarriorTrading")
    Bot.MostRetweetHighestScoredTweet()

if __name__ == "__main__":
    main()