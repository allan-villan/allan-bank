from database import BankDatabase
from bank import Accounts, Services

if __name__ == '__main__':
    running = True
    
    while running:
        print("\nWelcome to the main menu.\n")
        print("Please choose an option to continue:\n")
        choice = int(input("1: Open an Account\n"
                           "2: Log in\n"
                           "3: Exit\n")
        )
        
        # if the user wants to open an account
        if choice == 1:
            print("Thank you for choosing AllanBank! To begin, we're going to need a few details...")
            print("\nAre you an employee with AllanBank?")
            user_choice = int(input("Enter 1 for yes, 2 for no\n"))
            
            # checks to see if it is an employee
            if user_choice == 1:
                BankDatabase.create_employee_table()
                print("\n\n\nThank you for joining us as a valuable team member!")

                # Gets all necessary information
                first_name = str(input("\nLet's start with your First Name: "))
                last_name = str(input("\nNext, we'll need your Last Name: "))
                home_address = str(input("\nNow, we need your Home Address: "))
                role = str(input("\nWhat role do you have within the company?: "))
                salary = float(input("\nFinally, what was the agreed upon salary?: "))

                employee_id = BankDatabase.add_employee(first_name, last_name, home_address, role, salary)

                print("\n\n\n")
                print("    Account successfully created\n")
                print("!!!PLEASE KEEP YOUR EMPLOYEE_ID TO LOG IN!!!\n")
                print("    Your Employee ID is: {}\n".format(employee_id))

            # Checks to see if user is a customer
            elif user_choice == 2:
                BankDatabase.create_customer_table()
                print("\nThank you for joining us!")

                # Gets all necessary information
                first_name = str(input("\nLet's start with your First Name: "))
                last_name = str(input("\nNext, we'll need your Last Name: "))
                home_address = str(input("\nNow, we need your Home Address: "))
                checkings_balance = float(input("\nFinally, we'll need your Initial Deposit: "))

                user_id = BankDatabase.add_customer(first_name, last_name, home_address, checkings_balance)

                print("\n\n\n")
                print("    Account successfully created\n")
                print("!!!PLEASE KEEP YOUR USER_ID TO LOG IN!!!\n")
                print("    Your User ID is: {}\n".format(user_id))

            # If user did not enter 1 or 2 
            else:
                raise Exception("Please only enter 1 for Employees, 2 for Customers")
            
        # If the user is returning
        elif choice == 2:
            print("\nAre you an employee with AllanBank?")
            user_choice = int(input("Enter 1 for yes, 2 for no\n"))
            
            # Checks to see if it is an employee
            if user_choice == 1:
                print("\n\n\n")
                print("Welcome back to AllanBank!\n")
                print("Please enter the following information...\n")
                first_name = str(input("First Name: "))
                last_name = str(input("Last Name: "))
                empoyee_id = int(input("Employee ID: "))

                details = BankDatabase.employee_login(first_name, last_name, employee_id)

                # Checks if employee_login method returned employee_id
                if details is not None:
                    open = True

                while open:
                    print("\n\n\n")
                    user_choice = int(input(
                    """Pick something to do: 
                    1) Apply for a promotion
                    2) Grant a customer a credit card
                    3) Grant a customer a loan
                    4) Exit
                    """))

                    # If employee wants to apply for promotion
                    if user_choice == 1:
                        years = int(input("How many years have you been working at AllanBank?\n"))
                        
                        # If the employee worked for less than a year, they don't qualify
                        if years < 1:
                            print("You need to work here for at least 1 year to qualify for a promotion.")
                            print("Please reapply for a promotion after working here for 1 year!")

                        # If the customer qualified for a promotion
                        else:
                            print("Congratulations {} {}! You qualify for a promotion!".format(first_name, last_name))
                            print("You will be placed in a list of candidates. Good luck!!")

                            promotion_list = {
                                "First Name": first_name,
                                "Last Name": last_name,
                                "Employee ID": employee_id,
                                "Role": role
                            }

                    # Employee wants to begin creditcard process for customer
                    elif user_choice == 2:
                        first_name = str(input("\nPlease enter the first name of the customer: "))
                        last_name = str(input("\nPlease enter the last name of the customer: "))
                        user_id = str(input("\nPlease enter the customer's User ID: "))

                        decision = Services.grant_creditcard(first_name, last_name, user_id)

                        # If the customer qualifies for a creditcard
                        if decision == True:
                            print("Congratulations! {} {} qualifies for a credit card!".format(first_name, last_name))
                            print("They will be placed in a list of qualified candidates.")
                            print("Please inform them to check their mail within the next week for more information.")

                            creditcard_qualified = {
                                "First Name": first_name,
                                "Last Name": last_name,
                                "User ID": user_id
                            }
                        
                        # If the customer doesn't qualify for a loan
                        else:
                            print("Please reapply after you have a balance of $1,000.")
                        
                    # Employee wants to begin loan process for customer
                    elif user_choice == 3:
                        first_name = str(input("\nPlease enter the first name of the customer: "))
                        last_name = str(input("\nPlease enter the last name of the customer: "))
                        user_id = str(input("\nPlease enter the customer's User ID: "))

                        decision = Services.grant_loan(first_name, last_name, user_id)

                        # If the customer qualifies for a loan
                        if decision == True:
                            print("Congratulations! {} {} qualifies for a loan!".format(first_name, last_name))
                            print("They will be placed in a list of qualified candidates.")
                            print("Please inform them check their mail within the next week for more information.")

                            loan_qualified = {
                                "First Name": first_name,
                                "Last Name": last_name,
                                "User ID": user_id
                            }
                        
                        # If the customer does not qualify for a loan
                        else:
                            print("Please reapply after you have a balance of $10,000.")

                    # If employee wants to exit
                    elif user_choice == 4:
                        open = False

                    # Catches invalid responses
                    else:
                        raise Exception("Please enter a valid response")

            # Checks to see if it's a customer                
            elif user_choice == 2:
                print("\n\n\n")
                print("Welcome back to AllanBank!\n")
                print("Please enter the following information...\n")
                first_name = str(input("First Name: "))
                last_name = str(input("Last Name: "))
                user_id = int(input("User ID: "))

                details = BankDatabase.customer_login(first_name, last_name, user_id)

                if details is not None:
                    open = True
                while open:
                    print("\n\n\n")
                    user_choice = int(input(
                    """Pick something to do: 
                    1) Get Checkings Balance
                    2) Deposit to your Checkings Account
                    3) Withdraw from your Checkings Account
                    4) Exit
                    """))
                    
                    # User wants their checkings balance
                    if user_choice == 1:
                        balance = Accounts.get_checkings_balance(first_name, last_name, user_id)
                        print("\nYour current balance is: ${}".format(balance))

                    # User wants to deposit money into checkings account
                    elif user_choice == 2:
                        Accounts.deposit_checkings(first_name, last_name, user_id)
                        
                    # User wants to withdraw money from checkings account
                    elif user_choice == 3:
                        Accounts.withdraw_checkings(first_name, last_name, user_id)

                    # User wants to exit
                    elif user_choice == 4:
                        print("\nExiting...")
                        open = False

                    # Catches invalid responses
                    else:
                        raise Exception("Please enter a valid response")
            
            else:
                raise Exception("Please enter 1 if you are an employee, 2 if you are a customer")
        
        # User wants to exit out of program
        elif choice == 3:
            print("\nExiting...")
            running = False