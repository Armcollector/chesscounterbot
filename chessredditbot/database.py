import pyodbc
import config
def get_cursor_and_connection():
    cnxn = pyodbc.connect(config.connectionstring)
    # Create a cursor from the connection
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