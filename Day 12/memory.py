import sqlite3

db_name = "kanchha_memory.db"

def setup_db():
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
 #create a table if it doesn't exsist
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS memories(
    id INTEGER PRIMARY KEY AUTOINCREMENT ,
    category TEXT NOT NULL,
    content TEXT UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    
    """)

    conn.commit() #saves changes permanently 
    conn.close()
