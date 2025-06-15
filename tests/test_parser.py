from parser import parse_csv

def test_parse_csv():
    data = parse_csv("sample_data/invoices_sample.csv")
    assert isinstance(data, list)
    assert "vendor" in data[0]
