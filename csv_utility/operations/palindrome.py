import pandas as pd

def check_palindromes(data):
    """Check and display palindromes consisting solely of the letters A, D, V, B, N."""
    try:
        # Check if the dataset is empty
        if data.empty:
            print("The dataset is empty. No data to check.")
            return

        column_name = input("Enter column name to check for palindromes: ").strip()

        # Check if the column exists
        if column_name not in data.columns:
            print(f"Column '{column_name}' not found in the dataset.")
            return

        # Handle missing values
        if data[column_name].isnull().all():
            print(f"Column '{column_name}' contains only missing values. Cannot check for palindromes.")
            return
        elif data[column_name].isnull().any():
            print(f"Warning: Column '{column_name}' contains missing values. They will be ignored.")

        valid_chars = {'A', 'D', 'V', 'B', 'N'}
        palindromes = []

        # Iterate through non-null values in the column
        for value in data[column_name].dropna().astype(str):  # Ensure values are strings
            clean_value = value.upper().strip()  # Convert to uppercase & remove extra spaces

            # Check if all characters are valid
            if all(char in valid_chars for char in clean_value):
                # Check if it's a palindrome
                if clean_value == clean_value[::-1]:
                    palindromes.append(clean_value)

        # Display results
        if palindromes:
            print(f"Palindromes found in '{column_name}': {palindromes}")
            print(f"Total count of palindromes: {len(palindromes)}")
        else:
            print(f"No valid palindromes found in '{column_name}'.")

    except Exception as e:
        print(f"An error occurred: {e}")
