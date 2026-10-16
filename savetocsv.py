import csv
import os
from datetime import datetime
csv_file = "July2026.csv"

# ---Initialize csv file if it doesn't exist---


def initialize_csv():
    """Create a csv file with headers if it does not exist"""
    if not os.path.exists(csv_file):
        with open(csv_file, 'x', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Income", "Expense", "Savings", "I OWE", "OWED TO ME", "Category/More Info",
                            "Specific Item", "Amount", "Balance"])
            # empty line after header
            writer.writerow([])

# ---Save the income data to a csv file---


def save_data_to_csv(date, income, expense, savings, debt_owed, debt_given,
                     categoryorsource, specific_item, amount, balance):
    """saves collected input to a csv file"""
    with open(csv_file, 'a', newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, income, expense, savings, debt_owed, debt_given, categoryorsource,
                        specific_item, amount, balance])


initialize_csv()
