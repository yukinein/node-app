import snscrape.modules.twitter as sntwitter
import time

tempx = 0
for _ in iter(int, 1):
    i = 0
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper('#tesla').get_items()):
        if i > 0:
            break
        x = ([tweet.date, tweet.id, tweet.content])
        if tempx != x:
            print(x)
            tempx = x
            time.sleep(3)
