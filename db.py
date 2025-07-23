# import sqlite3

# DB_NAME = "todo.db"

# def get_db_connection():
#     connection = sqlite3.connect(DB_NAME)
#     connection.row_factory = sqlite3.Row  # Enable column access by name
#     return connection

# def init_db():
#     connection = get_db_connection()
#     cursor = connection.cursor()
#     cursor.execute(''' 
#         CREATE TABLE IF NOT EXISTS todos (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             task TEXT NOT NULL,
#             status TEXT DEFAULT 'Pending'
#         )
#     ''')
#     connection.commit()
#     connection.close()

# # Initialize DB if not exists
# if __name__ == "__main__":
#     init_db()





# import mysql.connector

# from secret_key import *

# def get_db_connection():
#     connection = mysql.connector.connect(
#         host     ="localhost",   # Your MySQL host
#         user     =db_username,   # Your MySQL username
#         password =db_password,   # Your MySQL password
#         database =db_name        # Database name
#     )
#     return connection



# in secrect.py
# db_username= "root"
# db_password = "Azsxdcf123@"
# db_name = "todos"