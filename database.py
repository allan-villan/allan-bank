import sqlite3
from sqlite3 import Error
import logging

class BankDatabase():
    logging.basicConfig(filename='logfile.log', encoding='utf-8', level=logging.DEBUG)

    def create_customer_table():
        try:
            conn = sqlite3.connect('bank.db')
        except Error as e:
            logging.error("Cannot connect to database...")
            print(e)
        cur = conn.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS customers (
                    first_name TEXT,
                    last_name TEXT,
                    home_address TEXT,
                    checkings_balance REAL)""")
        conn.commit()
        conn.close()

    
    def create_employee_table():
        try:
            conn = sqlite3.connect('bank.db')
        except Error as e:
            logging.error("Cannot connect to database...")
            print(e)
        cur = conn.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS employees (
                    first_name TEXT,
                    last_name TEXT,
                    home_address TEXT,
                    role TEXT,
                    salary REAL)""")
        conn.commit()
        conn.close()


    def add_customer(first_name: str, last_name: str, home_address: str, checkings_balance: float) -> int:
        try:
            conn = sqlite3.connect('bank.db')
        except Error as e:
            logging.error("Cannot connect to database...")
            print(e)
        cur = conn.cursor()
        cur.execute("INSERT INTO customers VALUES(?,?,?,?)", 
                    [first_name, last_name, home_address, checkings_balance])
        # Uses rowid as user_id
        user_id = cur.lastrowid
        conn.commit()
        conn.close()

        return user_id

    
    def add_employee(first_name: str, last_name: str, home_address: str, role: str, salary: float) -> int:
        try:
            conn = sqlite3.connect('bank.db')
        except Error as e:
            logging.error("Cannot connect to database...")
            print(e)
        cur = conn.cursor()
        # Inserts first name, last name, home address, and checkings balance into customers table
        cur.execute("INSERT INTO employees VALUES(?,?,?,?,?)",
                    [first_name, last_name, home_address, role, salary])
        # Uses rowid as user_id
        user_id = cur.lastrowid
        conn.commit()
        conn.close()

        return user_id

    
    def customer_login(first_name: str, last_name: str, user_id: int):
        try:
            conn = sqlite3.connect('bank.db')
        except Error as e:
            logging.error("Cannot connect to database...")
            print(e)
        cur = conn.cursor()
        # gets all available information if provided the proper login information
        cur.execute("SELECT * FROM customers WHERE first_name = '{}' AND last_name = '{}' AND rowid = '{}'"
                    .format(first_name, last_name, user_id))
        info = cur.fetchall()
        conn.commit()
        conn.close()

        if info == []:
            raise Error("Account not found")

        return info


    def employee_login(first_name: str, last_name: str, user_id: int):
        try:
            conn = sqlite3.connect('bank.db')
        except Error as e:
            logging.error("Cannot connect to database...")
            print(e)
        cur = conn.cursor()
        # gets all available information if provided the proper login information
        cur.execute("SELECT * FROM employees WHERE first_name = '{}' AND last_name = '{}' AND rowid = '{}'"
                    .format(first_name, last_name, user_id))
        info = cur.fetchall()
        conn.commit()
        conn.close()

        if info == []:
            raise Error("Account not found")

        return info


    def update_checkings(first_name: str, last_name: str, user_id: int, checkings_balance: float):
        try:
            conn = sqlite3.connect('bank.db')
        except Error as e:
            logging.error("Cannot connect to database...")
            print(e)
        cur = conn.cursor()
        cur.execute("""UPDATE customers SET checkings_balance = {}
                    WHERE rowid = {} AND first_name = '{}' AND last_name = '{}'"""
                    .format(checkings_balance, user_id, first_name, last_name))
        conn.commit()
        conn.close()