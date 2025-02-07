from csv_utility.utility import CSVUtility

def main():
    # Allow user to enter the CSV file name
    file_name = input("Enter the name of the CSV file: ").strip()

    try:
        # Initialize the utility with the CSV file
        csv_tool = CSVUtility(file_name)

        while True:
            print("\nCSV Utility Menu:")
            print("1. Display first few rows")
            print("2. Filter rows")
            print("3. Sort rows by a column")
            print("4. Aggregate data (sum, average, min, max)")
            print("5. Write modified data to a new CSV file")
            print("6. Check for palindromes")
            print("7. Exit")

            choice = input("Enter your choice (1-7): ").strip()

            if choice == '1':
                csv_tool.display_data()
            elif choice == '2':
                csv_tool.filter_rows() 
            elif choice == '3':
                csv_tool.sort_rows() 
            elif choice == '4':
                csv_tool.aggregate_data()
            elif choice == '5':
                csv_tool.write_to_new_file() 
            elif choice == '6':
                csv_tool.check_palindromes()
            elif choice == '7':
                print("Exiting the utility.")
                break
            else:
                print("Invalid choice. Please try again.")

            # Ask the user if they want to perform another operation
            next_action = input("\nDo you want to perform another operation? (yes/no): ").strip().lower()
            if next_action != 'yes':
                print("Exiting the utility.")
                break

    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found!")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
