import praw
import re


user_name = 'Armcollector'

client_id = 'PzVxWeeBhyn2-Q'
client_secret = 'RPw_4LXlwoPZQ2OAbUzP3Oux5pg'
user_agent = 'pc:chesscounterapp:0.1'

reddit = praw.Reddit(client_id=client_id,
            client_secret=client_secret,
            user_agent=user_agent)


c = None
for comment in reddit.subreddit('chess').comments():
    if not c:
        c = comment
        print(c.body)
        

    if re.search("(?i)reset the counter",c.body):
        print(c, c.body)

        
pass