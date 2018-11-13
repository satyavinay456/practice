import traceback
# Import the necessary package to process data in JSON format
print('yes')
try:
    import json
except ImportError:
    import simplejson as json

# We use the file saved from last step as example
tweets_filename = '/home/vinay/fetched_tweets.json'
tweets_file = open(tweets_filename, "r")
tweets_text = [] # We will store the text of every tweet in this list

target = open("tweetshastag.txt", 'w')
print('file opened')
for line in tweets_file:
    try:
        print('entered loop')
        # Read in one line of the file, convert it into a json object
        tweet = json.loads(line.strip())
        #print(tweet)
        if 'text' in tweet: # only messages contains 'text' field is a tweet
            #print(tweet['hashtags'])
            target.truncate()
            target.write( tweet['text'] )
            print(tweet['text'])

    except :
        traceback.print_exc()
        # read in a line is not in JSON format (sometimes error occured)
        continue
target.close()
