import savetocsv as s
from datetime import datetime
import financialsummary as f

# ---Gets all the necessary information from an expense---


def get_expenses():
    """
    Has all the features of the expenses
    """
    print('\n//EXPENSE SECTION//\n')
    # list containing categories within expenses
    category_list = ["🍉Food", "📚️School necessities",
                     "🔏Personal Items", "🛖Rent", "🏹goal_based expense",
                     "🚕Transport", "👚Clothing", "📳Utilities", "🏦Saving",
                     "🌴Miscellenious", "🤲Tithe"]

    print("Pick a category you want to fill for the expense")
    # enumerates the categories
    for i, category in enumerate(category_list, start=1):
        print(i, category)

    # A while loop that ensures the user enters the right input
    while True:

        category_input = input("Enter the expense category no.\n\t_")
        if category_input.isdigit():
            category_input = int(category_input)

            if category_input <= 0 or category_input > len(category_list):
                print("Please enter a number within the range")
                continue

            break
        else:
            print("please enter a number")
            continue

    # Matches the user input with the category
    category_pick = category_list[category_input - 1]

    # Asks for the specific item or service purchased
    category_item = input("Enter the item or service you purchased\n\t_")

    # Asks for the amount the user spent
    while True:
        amount = input("Enter the amount you spent\n\t_sh.")
        if amount.isdigit():
            amount = int(amount)

            if amount <= 0:
                print("Please enter the right figure")
                continue

            break
        else:
            print("please enter a number")

    # find bal
    bal = f.get_balance() - amount
    bal = round(bal, 2)

    # write to csv
    s.save_data_to_csv(datetime.now().strftime("%Y-%m-%d"),
                       '---', 'EXPENSE', "---", '---', '---', category_pick, category_item, amount, bal)

    print("\n---\nExpenses recorded successfully.\n---")
    print(f"Amount deducted sh.{amount}")
    print(f"NEW BAL: sh.{bal}")
