import sys
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

access_token = "1329248834-R3X8SrLzchMQyBOSRtV1QSJYfis2lidRex4RXeq"
access_token_secret = "g6pwJFjRJTQK2cRi01rGV3kpr6C9v7sQNTjrtPLtiETc4"
consumer_key = "l82JLsLffFzGMrytXhF4DAnf2"
consumer_secret = "Fh4985bvDNeF2RurZsseuDYBnbFv3cLmpdyyizFapBkr1uS954"


class StdOutListener(StreamListener):
    def on_data(self, data):
        print(data)
        with open('fetched_tweets.json', 'a') as tf:
            tf.write(data)
        return True


if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    stream.filter(track=['#iphone','#Samsung','#Moto','#Redmi','#Xiaomi','#Nokia','#lenovo','#oppo','#OnePlus','#BlackBerry','#HTC'])



