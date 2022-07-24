import sqlite3

# import mysql.connector
__cnx = None


def get_sql_connection():
    global __cnx
    if __cnx is None:
        __cnx = sqlite3.connect('ssip.db', check_same_thread=False)   # username- siddhant password-sid
        #you can access databse with SQLite browser

    # __cnx = mysql.connector.connect(user='root', password='Siddhant@001',
    #                                 host='127.0.0.1',
    #                              database='ssip')'''

    return __cnx
