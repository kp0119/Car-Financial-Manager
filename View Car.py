import subprocess
import csv
import os


def navigate_page():
    user_input = input("Type 1 to home otherwise type 2 to go to the monthly calculator: ")
    if user_input == "1":
        subprocess.run(["python", "Home Page.py"])
    elif user_input == "2":
        subprocess.run(["python", "Monthly Payment Page.py"])


def viewCar(carID=None, carName=None):
    if not os.path.exists('car_loan_info.csv'):
        print("File not found.")
        return

    with open('car_loan_info.csv', 'r') as spread:
        file = csv.reader(spread)
        for row in file:
            if (carID and row[0] == carID) or (carName and row[1] == carName):
                print(f"Car ID: {row[0]}")
                print(f"Car Name: {row[1]}")
                print(f"Car Price: {row[2]}")
                print(f"Loan Term: {row[3]}")
                print(f"Loan Amount: {row[4]}")
                print(f"Interest Rate: {row[5]}")
                navigate_page()
                return
    print("Car not found.")
    navigate_page()


def updateCar(carID=None, carName=None):
    if not os.path.exists('car_loan_info.csv'):
        print("File not found.")
        return

    rowUpdate = []
    updated = False

    with open('car_loan_info.csv', 'r') as spread:
        file = csv.reader(spread)
        for row in file:
            if (carID and row[0] == carID) or (carName and row[1] == carName):
                print("Below is your current information: ")
                print(f"Car ID: {row[0]}")
                print(f"Car Name: {row[1]}")
                print(f"Car Price: {row[2]}")
                print(f"Loan Term: {row[3]}")
                print(f"Loan Amount: {row[4]}")
                print(f"Interest Rate: {row[5]}")

                row[1] = input("Enter new car name: ")
                row[2] = input("Enter new car price: ")
                row[3] = input("Enter new loan term length: ")
                row[4] = input("Enter new loan amount: ")
                row[5] = input("Enter new interest rate: ")

                updated = True
            rowUpdate.append(row)

    if updated:
        with open('car_loan_info.csv', 'w', newline='') as spread:
            write = csv.writer(spread)
            write.writerows(rowUpdate)
        print("Your car information has been updated!")
    else:
        print("Car not found.")

    navigate_page()


def deleteCar(carID=None, carName=None):
    if not os.path.exists('car_loan_info.csv'):
        print("File not found.")
        return

    rowUpdate = []
    deleted = False

    with open('car_loan_info.csv', 'r') as spread:
        file = csv.reader(spread)
        for row in file:
            if (carID and row[0] == carID) or (carName and row[1] == carName):
                deleted = True
                continue
            rowUpdate.append(row)

    if deleted:
        with open('car_loan_info.csv', 'w', newline='') as spread:
            write = csv.writer(spread)
            write.writerows(rowUpdate)
        print("Your car has been deleted!")
    else:
        print("Car not found.")

    navigate_page()


def main():
    print("View Page:")

    user_input_1 = input("Type 1 to continue, otherwise type 2 to go home: ")
    if user_input_1 == "2":
        subprocess.run(["python", "Home Page.py"])
        return

    if user_input_1 == '1':
        user_input_2 = input("Type 1 if you would like to view your car using your car ID or 2 to view with car name: ")
        if user_input_2 == "1":
            carID = input("Please enter your car ID: ")
            carName = None
        elif user_input_2 == "2":
            carName = input("Please enter your car's nickname: ")
            carID = None

        user_input_3 = input(
            "Please type 1 if you'd like to view your car information 2 if you'd like to update your car "
            "information or 3 to delete your car: ")

        if user_input_3 == "1":
            viewCar(carID=carID, carName=carName)
        elif user_input_3 == "2":
            updateCar(carID=carID, carName=carName)
        elif user_input_3 == "3":
            confirm = input(
                "Please confirm that you would like to delete this vehicle by typing 1. Note that once you delete "
                "the vehicle, the data will no longer be there and will need to be entered again: ")
            if confirm == "1":
                deleteCar(carID=carID, carName=carName)


if __name__ == "__main__":
    main()
