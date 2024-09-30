import subprocess
import csv
import random


def saveInfo(carID, carName, carPrice, loanTerm, loanAmount, interestRate):
    with open('car_loan_info.csv', 'a', newline = '') as i:
        writer = csv.writer(i)
        writer.writerow([carID, carName, carPrice,loanTerm, loanAmount, interestRate])
        print("Your car and loan information has been added! Here is your cars entry ID (Note this ID can be used to "
              f"pull the cars information): {carID}")


print("Add Car Page:")

user_input_1 = input("Type 1 to continue, otherwise type 2 to go home: ")

if user_input_1 == "2":
    subprocess.run(["python", "Home Page.py"])

elif user_input_1 == "1":
    carID = random.randint(1,9999)
    carName = input("Please enter a car nickname: ")
    carPrice = input("Please enter your car price (Do not include dollar sign): ")
    loanTerm = input("Please input loan term length (Only type the number of months): ")
    loanAmount = input("Please enter your loan amount (Do not include dollar sign): ")
    interestRate = input("Please enter your loans interest rate (Only include the number): ")

    saveInfo(carID, carName, carPrice, loanTerm, loanAmount, interestRate)

    user_input_2 = input("Type 1 to return to the home screen, 2 to view, update or delete your entry or 3 to "
                         "calculate your monthly payment: ")

    if user_input_2 == "1":
        subprocess.run(["python", "Home Page.py"])

    elif user_input_2 == "2":
        subprocess.run(["python", "View Car.py"])

    elif user_input_2 == "3":
        subprocess.run(["python","Monthly Payment Page.py"])

