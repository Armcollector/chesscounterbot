import pyodbc
import config



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



def get_all_data():
    cursor, _ = get_cursor_and_connection()

    cursor.execute("""
    select * from test
    """)

    rows = cursor.fetchall()

    return [[row[0]] for row in rows]

if __name__ == '__main__':
    print(get_all_data())