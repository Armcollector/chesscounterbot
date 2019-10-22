import praw
import re
import config 
import database as database



reddit = praw.Reddit(client_id=config.client_id,
            client_secret=config.client_secret,
            user_agent=config.user_agent,
            username=config.username,
            password=config.password)



_subreddit = 'pythonforengineers'

c = None
cnt = 0
for comment in reddit.subreddit(_subreddit).comments(limit=1000):
    cnt +=1

    if re.search("(?i)reset the counter",comment.body):
        c = comment
        print(comment, comment.body, comment.created_utc)
        
        if database.submission_is_new(comment.submission.id):
            #database.record_submisson(comment.submission.id, comment.id, comment.submission.created_utc, 0, comment.created_utc, comment.submission.url)
            comment.reply("and here is the reply")

        
print(cnt)
pass

# <a href="https://i.redd.it/5x5bmab7fht31.png" target="_blank"><img alt="Post image" class="_2_tDEnGMLxpM6uOa2kaDB3 ImageBox-image media-element _1XWObl-3b9tPy64oaG6fax" src="https://i.redd.it/5x5bmab7fht31.png" style="max-height:700px"></a>