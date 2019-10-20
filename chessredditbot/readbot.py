import praw
import re
import config
import database



reddit = praw.Reddit(client_id=config.client_id,
            client_secret=config.client_secret,
            user_agent=config.user_agent)


c = None
cnt = 0
for comment in reddit.subreddit('chess').comments(limit=1000):
    cnt +=1

    if re.search("(?i)reset the counter",comment.body):
        c = comment
        print(comment, comment.body, comment.created_utc)
        
        if database.submission_is_new(comment.submission.id):
            print("is new")

        
print(cnt)
pass