import sqlite3

def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS UserLink
                 (uuid TEXT PRIMARY KEY, telegram_id INTEGER)''')
    conn.commit()
    conn.close()

def insert_user(uuid, telegram_id):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("INSERT INTO UserLink (uuid, telegram_id) VALUES (?, ?)", (uuid, telegram_id))
    conn.commit()
    conn.close()

def get_uuid(telegram_id):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT uuid FROM UserLink WHERE telegram_id = ?", (telegram_id,))
    uuid = c.fetchone()
    conn.close()
    return uuid[0] if uuid else None

def get_telegram_id(uuid):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT telegram_id FROM UserLink WHERE uuid = ?", (uuid,))
    telegram_id = c.fetchone()
    conn.close()
    return telegram_id[0] if telegram_id else None
