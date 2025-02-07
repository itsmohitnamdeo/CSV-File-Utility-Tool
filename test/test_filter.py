import pandas as pd
import pytest
from csv_utility.utility import filter_rows
@pytest.fixture
def sample_data():
    data = {
        "Date": ["2025-01-01", "2025-01-02", "2025-01-03", "2025-01-04", "2025-01-05"],
        "Product": ["Apple", "Banana", "Apple", "Orange", "Banana"],
        "Quantity": [10, 5, 15, 8, 12],
        "Price": [1.2, 0.8, 1.3, 1.5, 0.7]
    }
    return pd.DataFrame(data)

def test_filter_by_quantity(sample_data, monkeypatch):
    """Test filtering by numerical value in the 'Quantity' column."""
    inputs = iter(["Quantity", "num", "10", ">="])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    filtered_data = filter_rows(sample_data)
    
    assert len(filtered_data) == 3 
    assert all(filtered_data["Quantity"] >= 10)

def test_filter_by_product(sample_data, monkeypatch):
    """Test filtering by string value in the 'Product' column."""
    inputs = iter(["Product", "str", "Apple"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    filtered_data = filter_rows(sample_data)
    
    assert len(filtered_data) == 2
    assert all(filtered_data["Product"].str.contains("Apple", case=False))

def test_filter_invalid_column(sample_data, monkeypatch):
    """Test handling of invalid column name."""
    inputs = iter(["InvalidColumn"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    filtered_data = filter_rows(sample_data)
    
    assert filtered_data.equals(sample_data)
