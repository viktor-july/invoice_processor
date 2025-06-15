import sqlite3

def init_db(db_path):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS invoices (
        id INTEGER PRIMARY KEY,
        vendor TEXT,
        date TEXT,
        amount REAL
    )''')
    conn.commit()
    conn.close()

def save_invoice_data(db_path, data):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    for invoice in data:
        c.execute('INSERT INTO invoices (vendor, date, amount) VALUES (?, ?, ?)',
                  (invoice["vendor"], invoice["date"], invoice["amount"]))
    conn.commit()
    conn.close()
