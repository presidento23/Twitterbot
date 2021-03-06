import logging
import tweepy
from config import CreateApi
import datetime
import time
from random import randrange

logging.basicConfig(level = logging.INFO)
logger = logging.getLogger()

class Day_Trade_Listener():
    def __init__(self,api, who:str):
        self.api = api
        self.me = api.me()
        self.who = who

    def WhoSetter(self, b):
        self.who = b

    def WhoGetter(self):
        return self.who
    def MostHighestScoredTweet(self):
        Totalweight = {}
        Pastattentiongiventext = open("Attention.txt",'a+')
        try:
            Attentionids = Pastattentiongiventext.read().split()

        except:
            logger.error("Pastattentiongiven is empty")


        try:
            Last40tweets = (self.api.user_timeline(self.who, count=40))
            logger.info("40 tweets found")
        except Exception as e:
            logger.error(f"Error finding 40 tweets \n {e}" , exc_info=True)
            return

        for tweet in Last40tweets:
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
                    logger.error(f"Error retweeting {tweet.id}.{e}")
                return
            else:
                Totalweight[Temptotal] = tweet.id

        for tweet in sorted(Totalweight, key=Totalweight.get):
            try:
                self.api.retweet(Totalweight[tweet])
                logger.info(f"Retweeted {Totalweight[tweet]} with score of {tweet}")
                return
            except Exception as e:
                logger.error(f"Error retweeting {tweet}. \n {e}")
        return

    def GainAttention(self):
        # GainAttention primary purpose is to like the tweets of the influencer's followers to get more followers.
        # simply iterartors theorugh the influencers followers list and then through his follower(s) tweets and facvorites
        # 3 of them

        Pastattentiongiventext = open("Attention.txt",'a+')

        try:
            Attentionids = Pastattentiongiventext.read().split()

        except:
            logger.error("Pastattentiongiven is empty")


        try:
            self.Targetuserid = self.api.get_user(self.who).id
            logger.info(f"Found user {self.who}")

        except Exception as e:
            logger.error(f"Error locating usering in function GainAttention \n Error: {e}")
            return


        try:
            # to keep track of how many people has been targeted already.
            attentiongrabbed = 0


            for follower in tweepy.Cursor(self.api.followers, skip_status=True, id=self.Targetuserid).items():
                favoritecount = 0

                time.sleep(randrange(15,40))


                if follower.id in Attentionids:
                    logger.info(f"User {follower.id} was recently given attention")

                else:
                    Usertimeline = self.api.user_timeline(follower.id,count = 20)


                    # Iterators through the tweets of somebody timeline until it can favorite 3 or moves onto the next one
                    for tweet in Usertimeline:

                        try:
                            self.api.create_favorite(tweet.id)
                            logger.info(f"Favorited tweet {tweet.id} from {follower.id}")
                            favoritecount += 1
                            Pastattentiongiventext.write(f"{follower.id} \n")


                        except Exception as e:
                            logger.error(f"Couldn't favorite tweet {tweet.id} \n {e}")

                        logger.info(f"Grabbed {attentiongrabbed} people's attention. {3 - attentiongrabbed } remaining")

                        if favoritecount == 3 :
                            ts = time.time()
                            st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

                            Pastattentiongiventext.write(f"{follower.id} \n {st} \n")
                            break


                attentiongrabbed += 1
                if attentiongrabbed == 3:
                    logger.info(f"Successfully Grabbed {attentiongrabbed} people's attention")
                    Pastattentiongiventext.close()
                    return






        except Exception as e:

            logger.error (f"Error accessing {self.Targetuserid}'s followers. \n Error: {e}")








def main():
    api = CreateApi()
    Bot = Day_Trade_Listener(api, who = "WarriorTrading")

    while True:

        Bot.MostHighestScoredTweet()
        time.sleep(1200)
        Bot.MostHighestScoredTweet()
        time.sleep(randrange(3200, 7200))
        Bot.GainAttention()

if __name__ == "__main__":
    main()