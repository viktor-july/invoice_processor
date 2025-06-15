import os, tempfile
from database import init_db, save_invoice_data
from exporter import export_summary_to_excel

TEST_DATA = [{"vendor": "Test", "date": "2024-01-01", "amount": 123.45}]

def test_export():
    db_fd, db_path = tempfile.mkstemp()
    output = "test_summary.xlsx"
    init_db(db_path)
    save_invoice_data(db_path, TEST_DATA)
    export_summary_to_excel(db_path, output)
    assert os.path.exists(output)
    os.remove(output)
    os.close(db_fd)
