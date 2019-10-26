import sqlite3 as sql

from flask import Flask,render_template,request,redirect,url_for
import database
import praw
from datetime import datetime,timezone
import config
app = Flask(__name__)

DATABASE = 'database.db'

reddit = ""
refresh = None


@app.route("/")
def homepage():
    if not refresh:
        return redirect(url_for('login'))
    
    time_since_creation, image_link = database.get_latest()
    time_since_creation = str(datetime.now(timezone.utc) - datetime.fromtimestamp(time_since_creation,tz=timezone.utc))
    
    return render_template("front_page.html", time=time_since_creation, image=image_link)

@app.route('/login')
def login():
    global reddit

    reddit = praw.Reddit(
            client_id=config.client_id,
            client_secret=config.client_secret,
            user_agent=config.user_agent,
            redirect_uri='http://127.0.0.1:5000/authorize_callback'
            )

    return redirect(reddit.auth.url(["identity","submit"], "...","permanent"))

        

@app.route('/authorize_callback')
def authorized():
    global refresh
    code = request.args.get('code', '')

    refresh = reddit.auth.authorize(code)
        
    return redirect(url_for('homepage'))

if __name__ == "__main__":
    
    app.run()