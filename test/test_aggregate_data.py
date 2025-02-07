import pytest
import pandas as pd
from io import StringIO
from unittest.mock import patch
from csv_utility.utility import aggregate_data

csv_data = """Date,Product,Quantity,Price
2025-01-01,Apple,10,1.2
2025-01-02,Banana,5,0.8
2025-01-03,Apple,15,1.3
2025-01-04,Orange,8,1.5
2025-01-05,Banana,12,0.7
"""

data = pd.read_csv(StringIO(csv_data))

def test_valid_sum():
    """Test sum operation on a valid numeric column."""
    with patch("builtins.input", side_effect=["Quantity", "sum"]):
        assert aggregate_data(data) == 10 + 5 + 15 + 8 + 12

def test_valid_average():
    """Test average operation on a valid numeric column."""
    with patch("builtins.input", side_effect=["Price", "average"]):
        assert aggregate_data(data) == pytest.approx((1.2 + 0.8 + 1.3 + 1.5 + 0.7) / 5)

def test_valid_min():
    """Test min operation on a valid numeric column."""
    with patch("builtins.input", side_effect=["Quantity", "min"]):
        assert aggregate_data(data) == 5

def test_valid_max():
    """Test max operation on a valid numeric column."""
    with patch("builtins.input", side_effect=["Price", "max"]):
        assert aggregate_data(data) == 1.5

def test_non_numeric_column():
    """Test aggregation on a non-numeric column."""
    with patch("builtins.input", side_effect=["Product", "sum"]):
        assert aggregate_data(data) is None

def test_missing_column():
    """Test behavior when a non-existing column is entered."""
    with patch("builtins.input", side_effect=["UnknownColumn", "sum"]):
        assert aggregate_data(data) is None

def test_empty_dataset():
    """Test behavior when the dataset is empty."""
    empty_data = pd.DataFrame()
    with patch("builtins.input", side_effect=["Quantity", "sum"]):
        assert aggregate_data(empty_data) is None

def test_column_with_missing_values():
    """Test behavior when a column contains missing values."""
    data_with_nan = data.copy()
    data_with_nan.loc[2, "Quantity"] = None  # Inject a NaN value
    with patch("builtins.input", side_effect=["Quantity", "sum"]):
        assert aggregate_data(data_with_nan) == pytest.approx(10 + 5 + 8 + 12)

def test_column_with_all_missing_values():
    """Test behavior when a column contains only missing values."""
    data_all_nan = pd.DataFrame({"EmptyColumn": [None, None, None]})
    with patch("builtins.input", side_effect=["EmptyColumn", "sum"]):
        assert aggregate_data(data_all_nan) is None

def test_invalid_operation():
    """Test behavior when an invalid operation is entered."""
    with patch("builtins.input", side_effect=["Quantity", "invalid", "sum"]):
        assert aggregate_data(data) == 10 + 5 + 15 + 8 + 12
