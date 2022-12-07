import snscrape.modules.twitter as sntwitter
import pandas as pd

QUERY = "'pemerintah' 'gempa cianjur' lang:id"
tweets = []
LIMIT = 290
prevTweet = ''

for tweet in sntwitter.TwitterSearchScraper(QUERY).get_items():
  if len(tweets) == LIMIT:
    break
  else:
    if prevTweet != tweet.content:
      tweets.append([
        tweet,
        tweet.date,
        tweet.user.username,
        tweet.content
      ])
  prevTweet = tweet.content

df = pd.DataFrame(tweets, columns=['URL','Date', 'User', 'Tweet'])
df.to_csv('tweets-gempa-cianjur4.csv')
# print(df)
  # print(vars(tweet))
  # break
print(df)