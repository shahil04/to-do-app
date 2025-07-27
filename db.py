import sqlite3

DB_NAME = "todo.db"

def get_db_connection():
    connection = sqlite3.connect(DB_NAME)
    connection.row_factory = sqlite3.Row  # Enable column access by name
    print("success")
    return connection

def init_db():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS todos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL,
            status TEXT DEFAULT 'Pending'
        )
    ''')
    connection.commit()
    connection.close()

# Initialize DB if not exists
if __name__ == "__main__":
    init_db()


# ========================
# setup for render/

# import sqlite3
# import os

# # Use /tmp in Render, else current directory for Windows
# if os.getenv("RENDER"):
#     DB_PATH = "/tmp/todo.db"
# else:
#     DB_PATH = os.path.join(os.path.dirname(__file__), "todo.db")

# def get_db_connection():
#     # Ensure the directory exists (for local environments)
#     db_dir = os.path.dirname(DB_PATH)
#     if db_dir and not os.path.exists(db_dir):
#         os.makedirs(db_dir)

#     # Create DB and table if not exists
#     conn = sqlite3.connect(DB_PATH)
#     cursor = conn.cursor()
#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS todos (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             task TEXT NOT NULL,
#             status TEXT DEFAULT 'Pending'
#         )
#     """)
#     conn.commit()
#     return conn


# # Initialize DB if run directly
# if __name__ == "__main__":
#     conn = get_db_connection()
#     conn.close()
#     print(f"Database ready at {DB_PATH}")



