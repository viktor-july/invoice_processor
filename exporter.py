import pandas as pd
import sqlite3

def export_summary_to_excel(db_path, output_file):
    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query("SELECT vendor, SUM(amount) as total FROM invoices GROUP BY vendor", conn)
    df.to_excel(output_file, index=False)
    conn.close()