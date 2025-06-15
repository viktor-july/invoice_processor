import os, tempfile
from database import init_db, save_invoice_data

TEST_DATA = [{"vendor": "Test", "date": "2024-01-01", "amount": 123.45}]

def test_db_operations():
    db_fd, db_path = tempfile.mkstemp()
    init_db(db_path)
    save_invoice_data(db_path, TEST_DATA)
    os.close(db_fd)
    os.remove(db_path)
