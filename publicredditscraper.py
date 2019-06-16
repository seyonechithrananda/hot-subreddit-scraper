import praw
import time
import pandas as pd
import sys

# Author: {Seyone Chithrananda}
# Version: 1

print (sys.version)

#create github app (type - script) and enter secret, id, password, username and user_agent
r = praw.Reddit(client_id='',
client_secret='', password = '',
user_agent='r/MachineLearning scraper by /u/giftedapple', username ='giftedapple')

print(r.user.me())

ml_subreddit = r.subreddit('MachineLearning')
for posts in ml_subreddit.hot(limit=5):
    print(posts.title)

posts =[]

for post in ml_subreddit.hot(limit=5):
    posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])
posts = pd.DataFrame(posts,columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created'])
posts
print (posts)
posts.to_csv('top_ml_subreddit_posts.csv')
