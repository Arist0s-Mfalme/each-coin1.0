import debtandsavings as ds
import expense as e
import financialsummary as f
import income as i


def main():
    print("\n---EACHCOIN 1.0---\n")

    # List of services
    while True:
        print("1. Income\n"
              "2. Expense\n"
              "3. Debt\n"
              "4. Debt balanced\n"
              "5. Savings\n"
              "6. Total expenditure")

        user_pick = input("Pick a service(1,2,3,4,5,6)\t_")

        # Logic
        if user_pick == '1':
            i.get_income()
            break
        elif user_pick == "2":
            e.get_expenses()
            break
        elif user_pick == "3":
            ds.debt()
            break
        elif user_pick == "4":
            ds.debt_balanced()
            break
        elif user_pick == "5":
            ds.savings()
            break
        elif user_pick == "6":
            f.get_total()
            break
        else:
            print("Please enter the correct input")


if __name__ == "__main__":
    main()
