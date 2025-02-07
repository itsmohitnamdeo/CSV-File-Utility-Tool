import pandas as pd

def sort_rows(data):
    """Sort rows by a specific column."""
    try:
        # Display all rows and columns
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)

        # Check if the dataset is empty
        if data.empty:
            print("The dataset is empty. No data to sort.")
            return data

        column_name = input("Enter column name to sort by: ").strip()

        # Check if column exists
        if column_name not in data.columns:
            print(f"Column '{column_name}' does not exist in the dataset.")
            return data

        # Handle missing values in the selected column
        if data[column_name].isnull().all():
            print(f"Column '{column_name}' contains only missing values. Sorting is not possible.")
            return data

        # Determine sorting order
        while True:
            sort_order = input(f"Sort '{column_name}' in ascending or descending order? (Enter 'asc' or 'desc'): ").strip().lower()
            if sort_order in ['asc', 'desc']:
                ascending = (sort_order == 'asc')
                break
            else:
                print("Invalid input. Please enter 'asc' for ascending or 'desc' for descending.")

        try:
            sorted_data = data.sort_values(by=column_name, ascending=ascending, na_position='last')
        except TypeError:
            print(f"Column '{column_name}' contains mixed data types, which cannot be sorted reliably.")
            return data

        print("\nSorted Data:")
        print(sorted_data)

        return sorted_data 

    except Exception as e:
        print(f"Sorting failed: {e}")
        return data
