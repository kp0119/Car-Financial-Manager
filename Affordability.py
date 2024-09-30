import zmq
import json

def calculate_affordability(monthly_income, car_payment):
    percentage = (car_payment / monthly_income) * 100
    # determine if the car is affordable (payment <= 10% of monthly income)
    affordability = percentage <= 10
    # return a dictionary with the affordability result and percentage
    return {
        'affordability': affordability,
        'percentage': round(percentage, 2)  # round to 2 decimal places
    }

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5556")

print("Car Affordability Calculator Microservice is running...")

# main loop to continuously receive and process requests
while True:
    # wait for a message and parse it as JSON
    message = socket.recv_json()

    # extract monthly income and car payment from the message
    monthly_income = message.get('monthly_income')
    car_payment = message.get('car_payment')

    # check if required parameters are provided
    if monthly_income is None or car_payment is None:
        # if parameters are missing, send an error response
        response = {"error": "Missing required parameters"}
    else:
        # calculate affordability using the provided function
        response = calculate_affordability(monthly_income, car_payment)

    # send the response back to the client as JSON
    socket.send_json(response)
