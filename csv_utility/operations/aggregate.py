import pandas as pd

def aggregate_data(data):
    """Aggregate data by performing operations like sum, average, min, and max."""
    try:
        # Check if the dataset is empty
        if data.empty:
            print("The dataset is empty. No data to aggregate.")
            return None

        column_name = input("Enter column name to aggregate: ").strip()

        # Check if the column exists
        if column_name not in data.columns:
            print(f"Column '{column_name}' does not exist in the dataset.")
            return None

        # Check if the column contains numeric data
        if not pd.api.types.is_numeric_dtype(data[column_name]):
            print(f"Column '{column_name}' is not numeric. Aggregation cannot be performed.")
            return None

        # Handle missing values by warning the user
        if data[column_name].isnull().all():
            print(f"Column '{column_name}' contains only missing values. Cannot perform aggregation.")
            return None
        elif data[column_name].isnull().any():
            print(f"Warning: Column '{column_name}' contains missing values. They will be ignored in aggregation.")

        # Get user input for the aggregation operation
        valid_operations = {'sum': 'sum', 'average': 'mean', 'min': 'min', 'max': 'max'}
        while True:
            operation = input("Enter operation (sum, average, min, max): ").strip().lower()
            if operation in valid_operations:
                break
            print("Invalid operation. Please enter one of the following: sum, average, min, max.")

        # Perform the aggregation
        result = getattr(data[column_name], valid_operations[operation])()

        print(f"{operation.capitalize()} of '{column_name}': {result}")
        return result

    except Exception as e:
        print(f"An error occurred: {e}")
        return None
