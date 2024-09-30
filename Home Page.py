import subprocess
import zmq

# Monthly Payment Calculator Microservice port
def request_payment_service(action, carID=None, carName=None):
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5554")
    request = {
        "action": action,
        "carID": carID,
        "carName": carName
    }
    socket.send_json(request)
    response = socket.recv_json()
    return response

# Affordability Microservice port
def request_affordability_service(monthly_income, car_payment):
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5556")
    request = {
        "monthly_income": monthly_income,
        "car_payment": car_payment
    }
    socket.send_json(request)
    response = socket.recv_json()
    return response

# Help Page Microservice
def request_help_service():
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5557")

    request = {"action": "get_instructions"}
    socket.send_json(request)
    response = socket.recv_json()
    return response

# Budget Microservice
def request_budget_service(yearly_income):
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5558")
    request = {
        "action": "calculate_budget",
        "yearly_income": yearly_income
    }
    socket.send_json(request)
    response = socket.recv_json()
    return response

print("\nHome Page:")

print("Below are your options: \n"
      "1) Add Car and Loan information \n"
      "2) View Car and Loan information \n"
      "3) Monthly Payment \n"
      "4) Help \n"
      "5) What My Budget? \n"
      "6) Exit"
      )

user_input = input("Please enter a choice from above: ")

if user_input == "1":
    subprocess.run(["python", "Add Car.py"])

elif user_input == "2":
    subprocess.run(["python", "View Car.py"])

elif user_input == "3":
    user_input_2 = input("Type 1 if you would like to view your car using your car ID or 2 to view with car name: ")
    if user_input_2 == "1":
        carID = input("Please enter your car ID: ")
        response = request_payment_service("calculate", carID=carID)
    elif user_input_2 == "2":
        carName = input("Please enter your car's nickname: ")
        response = request_payment_service("calculate", carName=carName)

    if "error" in response:
        print(response["error"])
    else:
        car_payment = response['monthlyPayment']
        print(f"{response['carName']} monthly payment is ${car_payment:.2f}")

        monthly_income = float(input("Please enter your monthly income to see if its affordable: "))
        affordability_response = request_affordability_service(monthly_income, car_payment)

        if "error" in affordability_response:
            print(affordability_response["error"])
        else:
            affordability = "affordable" if affordability_response['affordability'] else "not affordable"
            print(f"The car payment is {affordability}. That is {affordability_response['percentage']}% of your monthly income.")

    user_input_3 = input("Type 1 to return home: ")
    if user_input_3 == "1":
        subprocess.run(["python", "Home Page.py"])

elif user_input == "4":
    help_response = request_help_service()
    if "instructions" in help_response:
        print(help_response["instructions"])
    else:
        print("No instructions available or an error occurred.")
    user_input_4 = input("Type 1 to return home: ")
    if user_input_4 == "1":
        subprocess.run(["python", "Home Page.py"])

elif user_input == "5":
    yearly_income = float(input("Please enter your yearly income: "))
    budget_response = request_budget_service(yearly_income)

    if "error" in budget_response:
        print(budget_response["error"])
    else:
        print(f"Your total car budget is ${budget_response['car_budget']:.2f}.")

    user_input_5 = input("Type 1 to return home: ")
    if user_input_5 == "1":
        subprocess.run(["python", "Home Page.py"])

elif user_input == "6":
    print("Exiting the program.")
    exit()

else:
    print("Invalid choice. Please enter a number from the options above.")
