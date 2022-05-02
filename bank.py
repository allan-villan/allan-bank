from database import BankDatabase
import sqlite3
from sqlite3 import Error

class Accounts():
    def get_checkings_balance(first_name, last_name, user_id) -> float:
        try:
            conn = sqlite3.connect('bank.db')
        except Error as e:
            print(e)
        cur = conn.cursor()
        # gets the checking balance for the account provided
        cur.execute("SELECT checkings_balance FROM customers WHERE first_name = '{}' AND last_name = '{}' AND rowid = '{}'"
                              .format(first_name, last_name, user_id))
        balance_tup = cur.fetchall()
        conn.commit()
        conn.close()

        # converts tuple into string, then a float to return balance as a float
        # allows balance to be altered depending on whether a user wants to deposit or withdraw money
        balance1 = str(balance_tup).replace(",","") 
        balance2 = str(balance1).replace("(","") 
        balance3 = str(balance2).replace(")","")
        balance4 = str(balance3).replace("[","")
        balance5 = str(balance4).replace("]","")

        return float(balance5)


    def deposit_checkings(first_name, last_name, user_id):
        # get balance
        balance = Accounts.get_checkings_balance(first_name, last_name, user_id)

        # get amount user wants to deposit
        amount = float(input("Please specify the amount you wish to deposit: $"))

        # filters invalid answers
        try:
            amount > 0
        except ValueError:
            print("Please enter a positive value")
        else:
            # after all checks, deposit money into checkings account
            balance += amount
        
        # commits changes to database
        BankDatabase.update_checkings(first_name, last_name, user_id, balance)

        print("\n\nSuccessfully deposited ${} to your account.".format(amount))
        print("\nYou have a new balance of: ${}".format(balance))


    def withdraw_checkings(first_name, last_name, user_id):
        # get balance
        balance = float(Accounts.get_checkings_balance(first_name, last_name, user_id))

        # prompt user for amount they want to withdraw
        amount = float(input("Please specify the amount you wish to withdraw: $"))

        # filters invalid answers
        try:
            amount > 0
        except ValueError:
            print("Please enter a positive value")
        else:
            try:
                amount > balance
            except ValueError:
                print("You cannot withdraw more than you own")
            else:
                # after all checks, withdraw money from checkings account
                balance -= amount

        # commits changes to database
        BankDatabase.update_checkings(first_name, last_name, user_id, balance)

        print("\n\nSuccessfully withdrew ${} from your account.".format(amount))
        print("\nYou have a new balance of: ${}".format(balance))


class Services():
    def grant_creditcard(first_name, last_name, user_id) -> bool:
        """
        | grant_creditcard checks if users has enough balance to open a card
        | to open a credit card, user needs at least $1,000 in their checkings account
        """
        # bool to decide whether user can open a credit card
        creditcard_auth = False

        # get balance to determine if user is eligible
        balance = Accounts.get_checkings_balance(first_name, last_name, user_id)

        # checks balance to see if user qualifies
        if balance >= 1000:
            creditcard_auth = True
        else:
            print("Insufficient funds to qualify for a credit card...")

        # returns bool
        return creditcard_auth


    def grant_loan(first_name, last_name, user_id) -> bool:
        """
        | grant_loan checks if users has enough balance to open a loan
        | to open a loan, user needs at least $10,000 in their checkings account
        """
        # bool to decide whether user can open a loan
        loan_auth = False

        # get balance to determine if user is eligible
        balance = Accounts.get_checkings_balance(first_name, last_name, user_id)

        # checks balance to see if user qualifies
        if balance >= 10000:
            loan_auth = True
        else:
            print("Insufficient funds to qualify for a loan...")

        # returns bool
        return loan_auth