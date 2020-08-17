import logging

from config import CreateApi

logging.basicConfig(level = logging.INFO)
logger = logging.getLogger()

class Day_Trade_Listener():
    def __init__(self,api):
        self.api = api
        self.me = api.me()

    def MostRecentTweet(self, who):

        if isinstance(who,str):
            print(self.api.user_timeline(who, count = 30))



def main():
    api = CreateApi()
    Bot = Day_Trade_Listener(api)
    Bot.MostRecentTweet("WarriorTrading")

if __name__ == "__main__":
    main()