import sqlite3 as sql

from flask import Flask,render_template
import database
from datetime import datetime,timezone
app = Flask(__name__)

DATABASE = 'database.db'

@app.route("/")
def hello():

    time_since_creation, image_link = database.get_latest()

    time_since_creation = str(datetime.now(timezone.utc) - datetime.fromtimestamp(time_since_creation,tz=timezone.utc))
    

    return render_template("front_page.html", time=time_since_creation, image=image_link)
    

if __name__ == "__main__":
    
    app.run(host='0.0.0.0')