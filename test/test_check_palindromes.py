import pandas as pd
import pytest
from csv_utility.utility import check_palindromes
@pytest.fixture
def sample_data():
    """Sample dataset for testing palindrome detection."""
    data = pd.DataFrame({
        "Words": ["ADA", "VAV", "BANANA", "DAD", "NAN", "ABC", "ABBA", None, "ADVBA"]
    })
    return data

def test_check_valid_palindromes(sample_data, capsys, monkeypatch):
    """Test function for detecting valid palindromes consisting of 'A, D, V, B, N'."""
   
    monkeypatch.setattr('builtins.input', lambda _: "Words")
    check_palindromes(sample_data)
    captured = capsys.readouterr()
    expected_palindromes = ["ADA", "VAV", "DAD", "NAN", "ABBA"]
    for palindrome in expected_palindromes:
        assert palindrome in captured.out, f"Missing expected palindrome: {palindrome}"
    assert f"Total count of palindromes: {len(expected_palindromes)}" in captured.out


def test_check_no_valid_palindromes(sample_data, capsys, monkeypatch):
    """Test case when no valid palindromes exist."""
    new_data = pd.DataFrame({"Words": ["XYZ", "123", "HELLO", "WORLD"]})
    monkeypatch.setattr('builtins.input', lambda _: "Words")
    check_palindromes(new_data)
    captured = capsys.readouterr()
    assert "No valid palindromes found" in captured.out

def test_column_not_found(sample_data, capsys, monkeypatch):
    """Test case when a non-existent column is entered."""
    monkeypatch.setattr('builtins.input', lambda _: "InvalidColumn")
    check_palindromes(sample_data)
    captured = capsys.readouterr()
    assert "Column 'InvalidColumn' not found in the dataset." in captured.out

def test_empty_dataset(capsys, monkeypatch):
    """Test case when an empty DataFrame is given."""
    empty_data = pd.DataFrame()
    monkeypatch.setattr('builtins.input', lambda _: "Words")
    check_palindromes(empty_data)
    captured = capsys.readouterr()
    assert "The dataset is empty. No data to check." in captured.out
