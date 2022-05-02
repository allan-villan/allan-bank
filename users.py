from database import BankDatabase

class Customer():
    """
    | The Customer class takes in three arguemnts:
    | 1) First Name
    | 2) Last Name
    | 3) Home Address
    | 4) Checkings Balance
    | 
    | Try statements make sure Checkings and Savings balance are valid entries
    | After checking Checkings balance for errors
    """
    def __init__(self, first_name: str, last_name: str, home_address: str, checkings_balance=0.0):
        self.first_name = first_name
        self.last_name = last_name
        self.home_address = home_address
        self.checkings_balance = checkings_balance

        # check checkings balance if valid
        try:
            self.checkings_balance < 0
        except ValueError:
            print("Invalid checkings balance. Try again.")

        
        BankDatabase.create_table()
        BankDatabase.add_customer(first_name, last_name, home_address, checkings_balance)


class Employee():
    """
    | The Employee class takes in four arguemnts:
    | 1) First Name
    | 2) Home Address
    | 3) Current Role
    | 4) Salary
    """
    def __init__(self, first_name: str, last_name: str, home_address: str, role: str, salary=0.0):
        self.first_name = first_name
        self.last_name = last_name
        self.home_address = home_address
        self.role = role
        self.salary = salary


    def get_role(self) -> str:
        print("{} {}'s current role: {}".format(self.f_name, self.l_name, self.role))
        return self.role

    
    def get_salary(self) -> float:
        print("{} {}'s current role: {}".format(self.f_name, self.l_name, self.salary))
        return self.salary
