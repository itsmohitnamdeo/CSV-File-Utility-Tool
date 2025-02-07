import pandas as pd

def filter_rows(data):
    """Filter rows based on user-defined criteria."""
    try:
        # Display all rows
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)

        # Check if DataFrame is empty
        if data.empty:
            print("The dataset is empty. No data to filter.")
            return data

        column_name = input("Enter the column name to filter by: ").strip()

        if column_name not in data.columns:
            print(f"Column '{column_name}' does not exist in the dataset.")
            return data

        filtered_data = data.copy()

        # Handle missing values
        if filtered_data[column_name].isnull().all():
            print(f"Column '{column_name}' contains only missing values. No filtering possible.")
            return data

        while True:
            condition_type = input("Do you want to filter by numerical or string condition? (Enter 'num' or 'str'): ").strip().lower()

            if condition_type == 'num':
                temp_column = pd.to_numeric(filtered_data[column_name], errors='coerce')

                if temp_column.isnull().all():
                    print(f"Column '{column_name}' is not numeric. Please choose a valid numeric column.")
                    continue 

                try:
                    threshold = float(input(f"Enter the threshold for filtering '{column_name}': ").strip())
                    operator = input(f"Enter the operator for comparison (>, <, >=, <=, ==, !=): ").strip()

                    valid_operators = {'>', '<', '>=', '<=', '==', '!='}
                    if operator not in valid_operators:
                        print("Invalid operator. Please use one of the following: >, <, >=, <=, ==, !=.")
                        continue 

                    # Apply the filter condition
                    filtered_data = filtered_data[temp_column.astype(float).map(eval(f"lambda x: x {operator} {threshold}"))]
                    break 

                except ValueError:
                    print("Invalid input. Please enter a valid numeric threshold.")
                    continue 

            elif condition_type == 'str':
                # Ensure column is string type
                if not pd.api.types.is_string_dtype(filtered_data[column_name]):
                    print(f"Column '{column_name}' is not a string column. Please choose a valid string column.")
                    continue 

                substring = input(f"Enter the substring to filter '{column_name}' by: ").strip()
                filtered_data = filtered_data[filtered_data[column_name].astype(str).str.contains(substring, case=False, na=False)]
                break

            else:
                print("Invalid input for condition type. Please enter 'num' or 'str'.")
                continue 

        if filtered_data.empty:
            print("No matching records found after filtering.")

        print("\nFiltered Data:")
        print(filtered_data)

        return filtered_data

    except Exception as e:
        print(f"An error occurred: {e}")
        return data
