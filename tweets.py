import snscrape.modules.twitter as sntwitter
import pandas as pd

query = "'world cup' lang:en until:2022-11-30 since:2022-11-01"
tweets = []
limit = 2000

for tweet in sntwitter.TwitterSearchScraper(query).get_items():
  if len(tweets) == limit:
    break
  else:
    tweets.append([
      tweet.date,
      tweet.user.username,
      tweet.content
    ])

df = pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet'])
df.to_csv('tweets.csv')
print(df)
  # print(vars(tweet))
  # break