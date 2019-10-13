import praw


user_name = 'Armcollector'

client_id = 'PzVxWeeBhyn2-Q'
client_secret = 'RPw_4LXlwoPZQ2OAbUzP3Oux5pg'
user_agent = 'pc:chesscounterapp:0.1'

reddit = praw.Reddit(client_id=client_id,
            client_secret=client_secret,
            user_agent=user_agent)


for comment in reddit.subreddit('chess').comments():
    print(comment)
    