import sqlite3
import os

# Creates games table if one, doesn't exist
def initialize_database():
    conn = sqlite3.connect("games.db")
    cursor = conn.cursor()

    base_dir = os.path.dirname(__file__)
    sql_path = os.path.join(base_dir, "database.sql")

    with open(sql_path, "r") as file:
        sql_script = file.read()

    cursor.executescript(sql_script)
    
    cursor.execute("SELECT * FROM games")
    rows = cursor.fetchall()
    print(rows)

    conn.commit()
    conn.close()

initialize_database()