import praw
import re
import config




reddit = praw.Reddit(client_id=config.client_id,
            client_secret=config.client_secret,
            user_agent=config.user_agent)


c = None
for comment in reddit.subreddit('chess').comments(limit=1000):
        

    if re.search("(?i)reset the counter",comment.body):
        c = comment
        print(comment, comment.body, comment.created_utc)
        

        
pass