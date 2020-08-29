# Twitter Fan Page Bot

This project creates a bot that will make a dedicated twitter fanpage of your favorite twitter influencers. It will retweet and favorite their best tweets and also will attract their followers to follow your page while you sit back and do nothing.


# Motivation

I saw a reddit post where a user created something similar and I decided to give myself a crack at it. This project primary purpose is to create a fanpage for influencers with a large enough following to benefit off of the followers you attract.

## Tech/Framework
**Built with**

-   [Python 3.8.5]([https://www.python.org/downloads/release/python-380/](https://www.python.org/downloads/release/python-380/))
- [Tweepy]([https://www.tweepy.org/](https://www.tweepy.org/))

## Features

- Adjustable frequency of retweeting and favoriting of tweets. 
- Behaves as if it was a human interacting with a user
- Run it in the background and forget about
- An algorthimic approach to finding the most popular tweets from a user

## 	 Code Example

    api = CreateApi() 
    

> INFO:root: API Created

    Bot.MostHighestScoredTweet()
	

> INFO:root: 40 tweets found
> INFO:root: Retweeted {tweet id} with a score of {tweet score} 

Note: tweet score should between 0 - 2

## Installation ( For Windows)

1. Download the repo. (Make sure you're in the folder you wish to download the repo in before running the below command)

    $ git clone https://github.com/presidento23/Twitterbot.git
 
2.  Change directories to the venv
	

    cd /venv

3. Download the requirements by running

    pip install -r requirements.txt
   
4. Make sure your virtual environment is setup.
 
## How to use?

To use this project simply open up the config file and enter your api  authorization information from twitter's developer website. Then open MainRun.py and click run. 

I would recommend checking your influencer's tweets first and getting a good range for how their tweets perform. For example if they're doing on average 50 retweets per tweet then I would adjust the algorithim accordingly. 

To do that open MainRun.py and scroll down until you see the variable

    Weightedretweetsscore
   
 Once you have that variable change the last number on that line to match their most amount of retweets. So if your influencer avearges 50 retweets per tweet then maybe put the number at 150.
Like this

    Weightedretweetsscore = (Tweetretweets - 0) / (150)

Same thing with favorites for the line below.

