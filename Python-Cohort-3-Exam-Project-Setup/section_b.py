# #Number 4
# # (a)


# def calculate_net_bonus_and_salary():
#     # Employee salary and years of service
#     salary = float(input("Enter your annual salary: "))
#     years_worked = int(input("Enter the number of years worked: "))
    
#     #Bonus based on the years worked
#     if years_worked > 4:
#         bonus_percentage = 8 / 100  
#     elif years_worked == 3:
#         bonus_percentage = 5 / 100  
#     else:
#         bonus_percentage = 0  
#     # Calculate the bonus amount and net salary
#     bonus_amount = salary * bonus_percentage
#     net_salary = salary + bonus_amount
    
#     print(f"Your bonus amount is: ${bonus_amount:.2f}")
#     print(f"Net salary amount is: ${net_salary:.2f}")


# calculate_net_bonus_and_salary()


#b#NUMBER 4(b)

class Sacco:
    def _init_(self):
        self.balance = 0

#deositing money
    def deposit(self, amount):
        if amount >= 1000:
            self.balance += amount
            print(f"Deposit of {amount} successfully made.")
        else:
            print("Minimum deposit amount is 1000.")

#withdrawing money
    def withdraw(self, amount):
        if amount >= 500 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal of {amount} successfully made.")
        elif amount < 500:
            print("Minimum withdrawal amount is 500.")
        else:
            print("Insufficient funds.")

#checking balance
    def check_balance(self):
        print(f"Your account balance is: {self.balance}")


def main():
    sacco = Sacco()
    print("Welcome  WITU Sacco")

    while True:
        print("\nMenu:")
        print("1. Deposit money")
        print("2. Withdraw money")
        print("3. Check balance")

#checking for input choices    
        choice = input("Enter your choice: ")

        if choice == '1':
            amount = float(input("Enter amount to deposit: "))
            sacco.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            sacco.withdraw(amount)
        elif choice == '3':
            sacco.check_balance()
        elif choice == '4':
            print("Thank you for using Witu Sacco.")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if _name_ == "_main_":
    main()


# (c)

import math

def calculate_d(X1, Y1, X2, Y2):
    x_squared = (X2 - X1) ** 2
    y_squared = (Y2 - Y1) ** 2
    d= math.sqrt(x_squared + y_squared)
    return d

def main():
    print("Enter the values of  (X1, Y1):")
    X1 = float(input("X1: "))
    Y1 = float(input("Y1: "))

    print("\nEnter the values of (X2, Y2):")
    X2 = float(input("X2: "))
    Y2 = float(input("Y2: "))

    
    d= calculate_d(X1, Y1, X2, Y2)

    
    print(f"\n The value of d between points ({X1}, {Y1}) and ({X2}, {Y2}) is: {d:.2f}")

if __name__ == "__main__":
    main()




