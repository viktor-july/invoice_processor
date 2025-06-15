from utils import validate_invoices

def test_validate():
    raw = [
        {"vendor": "A", "date": "2024-01-01", "amount": "100"},
        {"vendor": "", "date": "2024-01-01", "amount": "100"},
        {"vendor": "B", "date": "bad-date", "amount": "100"},
        {"vendor": "C", "date": "2024-01-01", "amount": "-50"},
    ]
    valid, rejected = validate_invoices(raw)
    assert len(valid) == 1
    assert len(rejected) == 3
