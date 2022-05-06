from database import BankDatabase

class Customer():
    def __init__(self, first_name: str, last_name: str, home_address: str, checkings_balance=0.0):
        self.first_name = first_name
        self.last_name = last_name
        self.home_address = home_address
        self.checkings_balance = checkings_balance

        try:
            self.checkings_balance < 0
        except ValueError:
            print("Invalid checkings balance. Try again.")

        BankDatabase.create_customer_table()
        BankDatabase.add_customer(self.first_name, self.last_name, self.home_address, self.checkings_balance)


class Employee():
    def __init__(self, first_name: str, last_name: str, home_address: str, role: str, salary=0.0):
        self.first_name = first_name
        self.last_name = last_name
        self.home_address = home_address
        self.role = role
        self.salary = salary

        BankDatabase.create_employee_table()
        BankDatabase.add_employee(self.first_name, self.last_name, self.home_address, self.role, self.salary)

    def get_role(self) -> str:
        print("{} {}'s current role: {}".format(self.first_name, self.last_name, self.role))
        return self.role

    
    def get_salary(self) -> float:
        print("{} {}'s current role: {}".format(self.first_name, self.last_name, self.salary))
        return self.salary
