import pandas as pd
import pytest
from csv_utility.utility import sort_rows
@pytest.fixture
def sample_data():
    """Sample dataset for testing sorting."""
    data = pd.DataFrame({
        "Date": ["2025-01-01", "2025-01-02", "2025-01-03", "2025-01-04", "2025-01-05"],
        "Product": ["Apple", "Banana", "Apple", "Orange", "Banana"],
        "Quantity": [10, 5, 15, 8, 12],
        "Price": [1.2, 0.8, 1.3, 1.5, 0.7]
    })
    return data

def test_sort_by_numeric_column(sample_data, monkeypatch):
    """Test sorting by a numeric column (Quantity) in ascending order."""

    inputs = iter(["Quantity", "asc"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs)) 

    sorted_data = sort_rows(sample_data)
    expected = sample_data.sort_values(by="Quantity", ascending=True)
    
    pd.testing.assert_frame_equal(sorted_data.reset_index(drop=True), expected.reset_index(drop=True))

def test_sort_by_string_column(sample_data, monkeypatch):
    """Test sorting by a string column (Product) in descending order."""

    inputs = iter(["Product", "desc"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs)) 

    sorted_data = sort_rows(sample_data)
    expected = sample_data.sort_values(by="Product", ascending=False)

    pd.testing.assert_frame_equal(sorted_data.reset_index(drop=True), expected.reset_index(drop=True))

def test_invalid_column_name(sample_data, monkeypatch):
    """Test handling of an invalid column name."""
    monkeypatch.setattr('builtins.input', lambda _: "InvalidColumn")

    sorted_data = sort_rows(sample_data)
    
    pd.testing.assert_frame_equal(sorted_data, sample_data)

def test_column_with_missing_values(sample_data, monkeypatch):
    """Test sorting when the selected column has only missing values."""
    sample_data["MissingColumn"] = [None, None, None, None, None]
    monkeypatch.setattr('builtins.input', lambda _: "MissingColumn") 

    sorted_data = sort_rows(sample_data)
    
    pd.testing.assert_frame_equal(sorted_data, sample_data)

