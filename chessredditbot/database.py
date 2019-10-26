import pyodbc
import chessredditbot.config as config
from datetime import datetime


def submission_is_new(submission_id):
    cursor, _ = get_cursor_and_connection()
    cursor.execute( "select count(*) from recorded_resets where submission = ?", submission_id )
    count = cursor.fetchone()

    return count[0] == 0


def record_submisson(submission_id, comment_id, submission_created_utc, record_created_utc, comment_created_utc, submission_url):
    cursor, cnxn = get_cursor_and_connection()
    cursor.execute("insert into recorded_resets values (?,?,?,?,?,?)",submission_id, comment_id, submission_created_utc, record_created_utc, comment_created_utc, submission_url )
    cnxn.commit()
    cnxn.close()



def get_cursor_and_connection():
    cnxn = pyodbc.connect(config.connectionstring)
    cursor = cnxn.cursor()
    return cursor, cnxn


def get_latest():
    cursor, _ = get_cursor_and_connection()

    cursor.execute("""
    select submision_created_utc, submission_url from recorded_resets
    where submision_created_utc = (select max(submision_created_utc) from recorded_resets)
    """)

    row = cursor.fetchone()

    return row


def log(log_text):
    cursor, cnxn = get_cursor_and_connection()

    cursor.execute("insert into chessredditbot_log values (?,?)",datetime.now(), log_text )
    cnxn.commit()
    cnxn.close()