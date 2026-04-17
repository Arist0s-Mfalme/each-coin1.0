import savetocsv as s
from datetime import datetime
import financialsummary as f
import json
import os

totals_file = "totals.json"


def load_totals():
    if not os.path.exists(totals_file):
        return {
            "total_savings": 0,
            "total_debt_owed": 0,
            "total_debt_given": 0
        }
    with open(totals_file, "r") as file:
        return json.load(file)


def save_totals(totals):
    with open(totals_file, "w") as file:
        json.dump(totals, file, indent=4)


def debt():
    print("\n//WELCOME TO DEBT SECTION//\n")

    d_query = input(
        "Pick an option\n"
        "1. Debt owed\n"
        "2. Debt received\t_"
    )
    d_person = input("Enter the Counterparty's name\n\t_")

    while True:
        if d_query == "1":
            try:
                d_amount = float(input("What was the amount lent\n\t_sh. "))
                bal = f.get_balance() - d_amount
                s.save_data_to_csv(
                    datetime.now().strftime("%Y-%m-%d"), "-",
                    "-", "-", "DEBT OWED", "-", d_person, "-",
                    d_amount, bal
                )
                # Update totals
                totals = load_totals()
                totals["total_debt_given"] += d_amount
                save_totals(totals)
                break
            except ValueError:
                print("Invalid input! Please enter a numeric value next time.")

        elif d_query == "2":
            try:
                d_amount = float(
                    input("What was the amount you received\n\t_sh. "))
                bal = f.get_balance() + d_amount
                s.save_data_to_csv(
                    datetime.now().strftime("%Y-%m-%d"), "-",
                    "-", "-", "-", "DEBT RECEIVED", d_person, "-",
                    d_amount, bal
                )
                # Update totals
                totals = load_totals()
                totals["total_debt_owed"] += d_amount
                save_totals(totals)
                break
            except ValueError:
                print("Invalid input! Please enter a numeric value next time.")

        else:
            print("Please enter a valid option (1 or 2).")
            d_query = input(
                "Pick an option\n"
                "1. Debt owed\n"
                "2. Debt received\t_"
            )


def debt_balanced():
    """Handles the debt owed that is paid back
    and the received I have paid back."""

    print("\n//WELCOME TO THE DEBT BALANCED SECTION//\n")

    d_query = input("Which account is being balanced\n"
                    "\t1. Debt owed\n"
                    "\t2. Debt received\t")

    d_person = input("Enter the counter parties name.\n\t_")

    while True:

        if d_query == "1":
            try:
                d_amount = float(
                    input("What was the amount lent\n\t_sh. "))
                bal = f.get_balance() + d_amount
                s.save_data_to_csv(
                    datetime.now().strftime("%Y-%m-%d"), "-",
                    "-", "-", "DEBT OWED", "-", d_person, "-",
                    -d_amount, bal
                )
                # Update totals
                totals = load_totals()
                totals["total_debt_given"] -= d_amount
                save_totals(totals)
                break
            except ValueError:
                print("Invalid input! Please enter a numeric value next time.")

        elif d_query == "2":
            try:
                d_amount = float(
                    input("What was the amount you received\n\t_sh. "))
                bal = f.get_balance() - d_amount
                s.save_data_to_csv(
                    datetime.now().strftime("%Y-%m-%d"), "-",
                    "-", "-", "-", "DEBT RECEIVED", d_person, "-",
                    -d_amount, bal
                )
                # Update totals
                totals = load_totals()
                totals["total_debt_owed"] -= d_amount
                save_totals(totals)
                break
            except ValueError:
                print("Invalid input! Please enter a numeric value next time.")

        else:
            print("Please enter a valid option (1 or 2).")
            d_query = input(
                "Pick an option\n"
                "1. Debt owed\n"
                "2. Debt received\t_"
            )


def savings():
    print("\n//Welcome to SAVINGS SECTION//\n")

    while True:
        try:
            amount = float(
                input("How much are you putting to savings\n\t_sh. "))
            bal = f.get_balance() - amount
            s.save_data_to_csv(
                datetime.now().strftime("%Y-%m-%d"), "-",
                "-", "SAVINGS", "-", "-", "-", "-",
                amount, bal
            )

            # Update totals
            totals = load_totals()
            totals["total_savings"] += amount
            save_totals(totals)
            break
        except ValueError:
            print("Invalid input! Please enter a numeric value.")
