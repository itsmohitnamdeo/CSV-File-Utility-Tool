def display_data(data):
    """Display the first few rows of the CSV."""
    try:
        # Check if the DataFrame is empty
        if data.empty:
            print("The dataset is empty. No data to display.")
            return
        
        # Ask user how many rows to display
        num_rows = input("How many rows would you like to display? (Enter a number): ").strip()

        # Validate if input is a number
        if not num_rows.isdigit():
            print("Invalid input. Please enter a valid positive number.")
            return
        
        num_rows = int(num_rows)

        if num_rows <= 0:
            print("Please enter a positive number greater than zero.")
            return
        
        # Display the first few rows with missing value indicators
        print(f"\nDisplaying first {num_rows} rows:")
        print(data.head(num_rows).fillna("[MISSING]"))  # Replaces NaN values with [MISSING]
        
    except Exception as e:
        print(f"An error occurred: {e}")
