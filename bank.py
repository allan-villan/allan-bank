from database import BankDatabase
import sqlite3
from sqlite3 import Error
import logging

class Accounts():
    def get_checkings_balance(first_name, last_name, user_id) -> float:
        try:
            conn = sqlite3.connect('bank.db')
        except Error as e:
            logging.error("Cannot connect to database...")
            print(e)
        cur = conn.cursor()
        cur.execute("SELECT checkings_balance FROM customers WHERE first_name = '{}' AND last_name = '{}' AND rowid = '{}'"
                              .format(first_name, last_name, user_id))
        balance_tup = cur.fetchall()
        conn.commit()
        conn.close()

        # Converts tuple received from database into str to strip chacacters so we can convert to float
        balance = str(balance_tup).strip("[(,)]")

        return float(balance)


    def deposit_checkings(first_name, last_name, user_id):
        balance = Accounts.get_checkings_balance(first_name, last_name, user_id)
        amount = float(input("Please specify the amount you wish to deposit: $"))

        try:
            amount > 0
        except ValueError:
            print("Please enter a positive value")
        else:
            balance += amount
        
        BankDatabase.update_checkings(first_name, last_name, user_id, balance)

        print("\n\nSuccessfully deposited ${} to your account.".format(amount))
        print("\nYou have a new balance of: ${}".format(balance))


    def withdraw_checkings(first_name, last_name, user_id):
        balance = float(Accounts.get_checkings_balance(first_name, last_name, user_id))
        amount = float(input("Please specify the amount you wish to withdraw: $"))

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
                balance -= amount

        BankDatabase.update_checkings(first_name, last_name, user_id, balance)

        print("\n\nSuccessfully withdrew ${} from your account.".format(amount))
        print("\nYou have a new balance of: ${}".format(balance))


class Services():
    def grant_creditcard(first_name, last_name, user_id) -> bool:
        """Returns a bool to determine if user can receive a creditcard

        grant_creditcard checks if users has enough balance to open a card
        To open a credit card, user needs at least $1,000 in their checkings account
        """
        creditcard_auth = False
        balance = Accounts.get_checkings_balance(first_name, last_name, user_id)

        if balance >= 1000:
            creditcard_auth = True
        else:
            raise ValueError("Insufficient funds to qualify for a credit card...")

        return creditcard_auth


    def grant_loan(first_name, last_name, user_id) -> bool:
        """Returns a bool to determine if user can receive loan

        grant_loan checks if users has enough balance to open a loan
        To open a loan, user needs at least $10,000 in their checkings account
        """
        loan_auth = False
        balance = Accounts.get_checkings_balance(first_name, last_name, user_id)

        if balance >= 10000:
            loan_auth = True
        else:
            raise ValueError("Insufficient funds to qualify for a loan...")

        return loan_auth