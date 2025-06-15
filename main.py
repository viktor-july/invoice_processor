
import argparse
from parser import parse_csv
from database import init_db, save_invoice_data
from exporter import export_summary_to_excel
from utils import validate_invoices, log_rejected

def main(input_csv, db_file, output_excel):
    init_db(db_file)
    raw_data = parse_csv(input_csv)
    validated_data, rejected = validate_invoices(raw_data)
    save_invoice_data(db_file, validated_data)
    export_summary_to_excel(db_file, output_excel)
    log_rejected(rejected)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Invoice Processor")
    parser.add_argument("input_csv", help="Path to input CSV file")
    parser.add_argument("db_file", help="Path to SQLite DB file")
    parser.add_argument("output_excel", help="Path to Excel summary output")
    args = parser.parse_args()
    main(args.input_csv, args.db_file, args.output_excel)
