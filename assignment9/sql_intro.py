import sqlite3
import os

db_path = "../db/magazines.db"
os.makedirs(os.path.dirname(db_path), exist_ok=True)

def create_tables(conn):
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = 1")
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS publishers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS magazines (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL,
            publisher_id INTEGER NOT NULL,
            FOREIGN KEY (publisher_id) REFERENCES publishers(id) ON DELETE CASCADE
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS subscribers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            address TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS subscriptions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            magazine_id INTEGER NOT NULL,
            subscriber_id INTEGER NOT NULL,
            expiration_date TEXT NOT NULL,
            FOREIGN KEY (magazine_id) REFERENCES magazines(id) ON DELETE CASCADE,
            FOREIGN KEY (subscriber_id) REFERENCES subscribers(id) ON DELETE CASCADE
        )
    ''')
    conn.commit()
    print("Tables ready.")

def add_publisher(conn, name):
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO publishers (name) VALUES (?)", (name,))
        conn.commit()
        print(f"Added publisher: {name}")
        return cursor.lastrowid
    except sqlite3.IntegrityError:
        cursor.execute("SELECT id FROM publishers WHERE name = ?", (name,))
        return cursor.fetchone()[0]

def add_magazine(conn, name, publisher_id):
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO magazines (name, publisher_id) VALUES (?, ?)", (name, publisher_id))
        conn.commit()
        print(f"Added magazine: {name}")
        return cursor.lastrowid
    except sqlite3.IntegrityError:
        cursor.execute("SELECT id FROM magazines WHERE name = ?", (name,))
        return cursor.fetchone()[0]

def add_subscriber(conn, name, address):
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM subscribers WHERE name = ? AND address = ?", (name, address))
    row = cursor.fetchone()
    if row:
        print(f"Subscriber '{name}' already exists. Using existing id.")
        return row[0]
    cursor.execute("INSERT INTO subscribers (name, address) VALUES (?, ?)", (name, address))
    conn.commit()
    print(f"Added subscriber: {name}")
    return cursor.lastrowid

def add_subscription(conn, magazine_id, subscriber_id, expiration_date):
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO subscriptions (magazine_id, subscriber_id, expiration_date) VALUES (?, ?, ?)",
                       (magazine_id, subscriber_id, expiration_date))
        conn.commit()
        print(f"Added subscription for subscriber {subscriber_id} to magazine {magazine_id} until {expiration_date}")
    except sqlite3.Error as e:
        print(f"Error adding subscription: {e}")

def main():
    conn = None
    try:
        conn = sqlite3.connect(db_path)
        print("Connected to database.")
        create_tables(conn)
        
        # Insert sample data
        pub_id1 = add_publisher(conn, "Penguin Random House")
        pub_id2 = add_publisher(conn, "Hachette Livre")
        pub_id3 = add_publisher(conn, "HarperCollins")
        
        mag_id1 = add_magazine(conn, "The New Yorker", pub_id1)
        mag_id2 = add_magazine(conn, "Paris Match", pub_id2)
        mag_id3 = add_magazine(conn, "Wired", pub_id3)
        
        sub_id1 = add_subscriber(conn, "Alice Johnson", "123 Maple St, Springfield")
        sub_id2 = add_subscriber(conn, "Bob Smith", "456 Oak Ave, Metropolis")
        sub_id3 = add_subscriber(conn, "Carol Davis", "789 Pine Rd, Gotham")
        
        add_subscription(conn, mag_id1, sub_id1, "2025-12-31")
        add_subscription(conn, mag_id2, sub_id1, "2025-06-30")
        add_subscription(conn, mag_id1, sub_id2, "2024-12-31")
        add_subscription(conn, mag_id3, sub_id3, "2025-01-15")
        add_subscription(conn, mag_id2, sub_id3, "2025-07-01")
        
        # Task 4: SQL Queries
        print("\n--- Task 4 Queries ---")
        cursor = conn.cursor()
        
        print("\nAll subscribers:")
        cursor.execute("SELECT * FROM subscribers")
        for row in cursor.fetchall():
            print(row)
        
        print("\nAll magazines sorted by name:")
        cursor.execute("SELECT * FROM magazines ORDER BY name")
        for row in cursor.fetchall():
            print(row)
        
        publisher_name = "Penguin Random House"
        cursor.execute('''
            SELECT magazines.name, publishers.name 
            FROM magazines 
            JOIN publishers ON magazines.publisher_id = publishers.id
            WHERE publishers.name = ?
        ''', (publisher_name,))
        rows = cursor.fetchall()
        print(f"\nMagazines published by '{publisher_name}':")
        for row in rows:
            print(row)
        
        print("\nData insertion and queries completed.")
        
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        if conn:
            conn.close()
            print("Connection closed.")

if __name__ == "__main__":
    main()