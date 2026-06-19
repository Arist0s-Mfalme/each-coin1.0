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
    print("\n//DEBT SECTION//\n")

    d_query = input(
        "Pick an option\n"
        "1. I OWE\n"
        "2. OWED TO ME\t_"
    )
    d_person = input("Enter the Counterparty's name\n\t_")

    while True:
        if d_query == "1":
            try:
                d_amount = float(input("What was the amount lent\n\t_sh. "))
                bal = f.get_balance() + d_amount
                s.save_data_to_csv(
                    datetime.now().strftime("%Y-%m-%d"), "-",
                    "-", "-", "I OWE", "-", d_person, "-",
                    d_amount, bal
                )
                # Update totals
                totals = load_totals()
                totals["total_i_owe"] += d_amount
                save_totals(totals)

                # USER DISPLAY
                print(f"Amount I OWE sh.{d_amount}")
                print(f"NEW TOTAL I OWE BAL sh.{totals['total_i_owe']}")
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
                    "-", "-", "-", "OWED TO ME", d_person, "-",
                    d_amount, bal
                )
                # Update totals
                totals = load_totals()
                totals["total_owed_to_me"] += d_amount
                save_totals(totals)

                # USER DISPLAY
                print(f"Amount OWED TO ME sh.{d_amount}")
                print(f"NEW TOTAL OWED TO ME sh.{totals['total_owed_to_me']}")
                break

            except ValueError:
                print("Invalid input! Please enter a numeric value next time.")

        else:
            print("Please enter a valid option (1 or 2).")
            d_query = input(
                "Pick an option\n"
                "1. I OWE\n"
                "2. OWED TO ME\t_"
            )


def debt_balanced():
    """
    Handles the debt owed that is paid back
    and the received I have paid back.
    """

    print("\n//DEBT BALANCED SECTION//\n")

    d_query = input("Which account is being balanced\n"
                    "\t1. I OWE\n"
                    "\t2. OWED TO ME\n\t\t_")

    d_person = input("Enter the counter parties name.\n\t_")

    while True:

        if d_query == "1":
            try:
                d_amount = float(
                    input("What was the amount lent\n\t_sh. "))
                bal = f.get_balance() - d_amount
                s.save_data_to_csv(
                    datetime.now().strftime("%Y-%m-%d"), "-",
                    "-", "-", "I OWE", "-", d_person, "-",
                    -d_amount, bal
                )
                # Update totals
                totals = load_totals()
                totals["total_i_owe"] -= d_amount
                save_totals(totals)

                # USER DISPLAY
                print(f"Amount I OWE sh.{d_amount}")
                print(f"NEW TOTAL I OWE BAL sh.{totals['total_i_owe']}")
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
                    "-", "-", "-", "OWED TO ME", d_person, "-",
                    -d_amount, bal
                )
                # Update totals
                totals = load_totals()
                totals["total_owed_to_me"] -= d_amount
                save_totals(totals)

                # USER DISPLAY
                print(f"Amount OWED TO ME sh.{d_amount}")
                print(f"NEW TOTAL OWED TO ME sh.{totals['total_owed_to_me']}")
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
    '''
    Contains all the savings Logic
    '''
    print("\n//SAVINGS SECTION//\n")
    s_quiry = input("1. Deposit\n"
                    "2. Withdraw(1 or 2)\n\t_")

    if s_quiry == "1":
        while True:
            amount = input("Deposit amount\n\t_sh. ")

            # confirm if digit
            if amount.isdigit():
                amount = float(amount)
            else:
                print("Invalid input! Please enter a numeric value.")
                continue

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

            # USER DISPLAY
            print(f"Amount deposited sh.{amount}")
            print(f"NEW SAVING BALANCE sh.{totals['total_savings']}")
            break

    elif s_quiry == '2':
        while True:
            amount = input("Withdraw amount\n\t_sh. ")

            # confirm if digit
            if amount.isdigit():
                amount = float(amount)
            else:
                print("Invalid input! Please enter a numeric value.")
                continue

            bal = f.get_balance() + amount
            s.save_data_to_csv(
                datetime.now().strftime("%Y-%m-%d"), "-",
                "-", "SAVINGS", "-", "-", "-", "-",
                amount, bal
            )

            # Update totals
            totals = load_totals()
            totals["total_savings"] -= amount
            save_totals(totals)

            # USER DISPLAY
            print(f"Amount withdrawn sh.{amount}")
            print(f"NEW SAVING BALANCE sh.{totals['total_savings']}")
            break
