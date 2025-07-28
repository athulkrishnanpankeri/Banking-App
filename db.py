import sqlite3

DATABASE_NAME = "bank.db"

def create_table():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            transaction_date TEXT NOT NULL,
            description TEXT NOT NULL,
            amount REAL NOT NULL,
            transaction_type TEXT NOT NULL,
            category TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_transaction(transaction_date, description, amount, transaction_type, category):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO transactions (transaction_date, description, amount, transaction_type, category)
        VALUES (?, ?, ?, ?, ?)
    ''', (transaction_date, description, amount, transaction_type, category))
    conn.commit()
    conn.close()

def view_transactions(trans_type=None, category=None):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    sql_query = "SELECT transaction_date, description, amount, transaction_type, category FROM transactions"
    conditions = []
    params = []

    if trans_type:
        conditions.append("transaction_type = ?")
        params.append(trans_type)
    if category:
        conditions.append("category = ?")
        params.append(category)

    if conditions:
        sql_query += " WHERE " + " AND ".join(conditions)

    sql_query += " ORDER BY transaction_date DESC;"

    cursor.execute(sql_query, params)
    rows = cursor.fetchall()
    conn.close()
    return rows
