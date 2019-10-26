import sqlite3 as sql

from flask import Flask,render_template,request,redirect,url_for
import database
import praw
from datetime import datetime,timezone
import config
app = Flask(__name__)

DATABASE = 'database.db'

the_token = ""
reddit = ""

@app.route("/")
def homepage():
    global reddit
    if not the_token:
        
        reddit = praw.Reddit(
            client_id=config.client_id,
            client_secret=config.client_secret,
            user_agent=config.user_agent,
            redirect_uri='http://127.0.0.1:5000/authorize_callback'
            )


        text = f' I dont have the token: <a href="{reddit.auth.url(["identity"], "...","permanent")} "> Click to login </a>'

        
        
    else:
        text =" I do have the token "
        refresh = reddit.auth.authorize(the_token)
        text += str(reddit.user.me())
    
    return text

    #time_since_creation, image_link = database.get_latest()

    #time_since_creation = str(datetime.now(timezone.utc) - datetime.fromtimestamp(time_since_creation,tz=timezone.utc))
    

    #return render_template("front_page.html", time=time_since_creation, image=image_link)
    

@app.route('/authorize_callback')
def authorized():
    global the_token
    code = request.args.get('code', '')

    the_token = code

    return redirect(url_for('homepage'))

if __name__ == "__main__":
    
    app.run()