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
