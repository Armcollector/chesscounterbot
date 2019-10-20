import sqlite3 as sql

from flask import Flask,render_template
app = Flask(__name__)

DATABASE = 'database.db'

@app.route("/")
def hello():
    return "Chessbot, front page"

@app.route('/list')
def list():
   con = sql.connect("database.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from students")
   
   rows = cur.fetchall()
   
   return render_template("list.html",rows = rows)



if __name__ == "__main__":
    app.run(host='0.0.0.0')