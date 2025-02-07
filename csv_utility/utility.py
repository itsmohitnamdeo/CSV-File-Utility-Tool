import pandas as pd
from csv_utility.operations.display import display_data
from csv_utility.operations.filter import filter_rows
from csv_utility.operations.sort import sort_rows
from csv_utility.operations.aggregate import aggregate_data
from csv_utility.operations.write import write_to_new_file
from csv_utility.operations.palindrome import check_palindromes


class CSVUtility:
    def __init__(self, file_name):
        self.file_name = file_name
        self.data = pd.read_csv(file_name)

    def display_data(self):
        display_data(self.data)

    def filter_rows(self):
        self.data = filter_rows(self.data) 

    def sort_rows(self):
        self.data = sort_rows(self.data)

    def aggregate_data(self):
        aggregate_data(self.data)

    def write_to_new_file(self):
        write_to_new_file(self.data)

    def check_palindromes(self):
        check_palindromes(self.data) 
