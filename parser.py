import csv

def parse_csv(file_path):
    invoices = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            invoices.append({
                "vendor": row.get("Vendor", "").strip(),
                "date": row.get("Date", "").strip(),
                "amount": row.get("Amount", "").strip()
            })
    return invoices
