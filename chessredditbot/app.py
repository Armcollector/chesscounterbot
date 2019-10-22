import sqlite3 as sql

from flask import Flask,render_template,request
import database
import praw
from datetime import datetime,timezone
import config
app = Flask(__name__)

DATABASE = 'database.db'

the_token = ""

@app.route("/")
def homepage():
    text = 'blah'


    if not the_token:
        
        reddit = praw.Reddit(
            client_id=config.client_id,
            client_secret=config.client_secret,
            user_agent=config.user_agent,
            redirect_uri='http://127.0.0.1:5000/authorize_callback'
            )


        text = f" I dont have the token: {reddit.auth.url(['identity'], '...','permanent')}"

        
        
    else:
        text =" I do have the token "

    # link_no_refresh = reddit.get_authorize_url('UniqueKey')
    # link_refresh = reddit.get_authorize_url('DifferentUniqueKey',
    #                                    refreshable=True)
    # link_no_refresh = "<a href=%s>link</a>" % link_no_refresh
    # link_refresh = "<a href=%s>link</a>" % link_refresh
    # text = "First link. Not refreshable %s</br></br>" % link_no_refresh
    # text += "Second link. Refreshable %s</br></br>" % link_refresh
    return text

    #time_since_creation, image_link = database.get_latest()

    #time_since_creation = str(datetime.now(timezone.utc) - datetime.fromtimestamp(time_since_creation,tz=timezone.utc))
    

    #return render_template("front_page.html", time=time_since_creation, image=image_link)
    

@app.route('/authorize_callback')
def authorized():
    state = request.args.get('state', '')
    code = request.args.get('code', '')
    #info = reddit.get_access_information(code)
    #user = reddit.get_me()
    info = "unknown info"
    user = "unknown user"
    variables_text = "State=%s, code=%s, info=%s." % (state, code,
                                                      info)
    
    the_token = code

    return variables_text + "<br><br>the correct code idiot: " + reddit.auth.authorize(code) + "<br><br>" + str(reddit.user.me())

if __name__ == "__main__":
    reddit = praw.Reddit(
            client_id=config.client_id,
            client_secret=config.client_secret,
            user_agent=config.user_agent,
            refresh_token=config.refresh_token
            )

    print(reddit.auth.scopes())
    

    app.run(debug=True, port=5000)