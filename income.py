import financialsummary as f
import savetocsv as s
from datetime import datetime
# ---gets all the necessary information from an income---


def get_income():
    """Has all features of income"""
    source = input("Enter the source of your income\n\t")
    while True:
        amount = input("Enter the amount you received\n\tsh.")
        if amount.isdigit():
            amount = int(amount)

            if amount <= 0:
                print("please enter the right figure")
                continue

            break

        else:
            print("please enter a valid number")

    # get bal
    bal = f.get_balance() + amount
    bal = round(bal, 2)

    # write to csv
    s.save_data_to_csv(datetime.now().strftime("%Y-%m-%d"), 'INCOME', '---', "---", "---", "---", source,
                       '----', amount, bal)

    print("\n---\nIncome recorded successfully.\n---")
    print(f"Amount incremented sh.{amount}")


