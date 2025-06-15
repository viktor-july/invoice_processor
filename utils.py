from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(message)s')

def validate_invoices(data):
    valid = []
    rejected = []
    for invoice in data:
        try:
            vendor = invoice["vendor"]
            date = datetime.strptime(invoice["date"], "%Y-%m-%d")
            amount = float(invoice["amount"])
            if vendor and amount > 0:
                valid.append({"vendor": vendor, "date": invoice["date"], "amount": amount})
            else:
                rejected.append(invoice)
        except Exception:
            rejected.append(invoice)
    return valid, rejected

def log_rejected(rejected):
    if rejected:
        logging.warning(f"Rejected {len(rejected)} invoice(s):")
        for r in rejected:
            logging.warning(r)
    else:
        logging.info("No invoices rejected.")
