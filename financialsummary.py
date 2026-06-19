import savetocsv
import os
import csv
from datetime import datetime

csv_file = savetocsv.csv_file
# ---get the bal---


def get_balance():

    if not os.path.exists(csv_file):
        return 0.0

    with open(csv_file, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        last_balance = 0.0
        for row in reader:
            try:
                last_balance = float(row["Balance"])
            except (ValueError, KeyError):
                continue
        return last_balance

# ---get the total for a certain period---


def get_total():
    print("Enter the start and end date (eg 2026-03-18)")
    start_date = input("\tSTART DATE: ")
    end_date = input("\tEND DATE: ")

    # convert input strings to date objects
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")

    # Get total expenses/ total income

    enquiry = input(
        "1.Total Income\n"
        "2.Total expenses, (1 or 2)\n\t_")

    # initialize total
    total = 0

    with open(csv_file, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            # convert raw date
            row_date = datetime.strptime(row["Date"], "%Y-%m-%d")

            # filter by date range
            if start <= row_date <= end:

                # filter by income or expense
                if enquiry == "1":
                    if row["Income"] == "INCOME":
                        amount = float(row["Amount"])
                        total += amount

                elif enquiry == "2":
                    if row["Expense"] == "EXPENSE":
                        amount = float(row["Amount"])
                        total += amount

                else:
                    print("Invalid input. Please enter a correct input.")
                    return None  # stop execution

        # USER DISPLAY
        print(f"\n---total amount sh.{total}---\n")

    return round(total, 2)
