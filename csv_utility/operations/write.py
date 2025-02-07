def write_to_new_file(data):
    """Write the modified data to a new CSV file."""
    output_file = input("Enter the name for the new CSV file: ").strip()
    data.to_csv(output_file, index=False)
    print(f"Data written to {output_file}")
