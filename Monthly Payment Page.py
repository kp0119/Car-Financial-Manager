import zmq
import csv

def calc(prin, rate, term):
    monthly = rate / 100 / 12
    pay = prin * (monthly * (1 + monthly) ** term) / ((1 + monthly) ** term - 1)
    return pay

def getCar(carIDs, carNames):
    with open('car_loan_info.csv', 'r') as spread:
        file = csv.reader(spread)
        for row in file:
            if (carIDs and row[0] == carIDs) or (carNames and row[1] == carNames):
                return {
                    "carName": row[1],
                    "carPrice": float(row[2]),
                    "loanTerm": int(row[3]),
                    "loanAmount": float(row[4]),
                    "interestRate": float(row[5])
                }

def main():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5554")

    print("Monthly Payment Service is running...")

    while True:
        message = socket.recv_json()
        if message['action'] == 'calculate':
            carIDs = message.get('carID')
            carNames = message.get('carName')
            calcCar = getCar(carIDs, carNames)
            if calcCar:
                monthPay = calc(
                    calcCar["loanAmount"],
                    calcCar["interestRate"],
                    calcCar["loanTerm"])
                response = {
                    "carName": calcCar["carName"],
                    "monthlyPayment": round(monthPay, 2)
                }
            else:
                response = {"error": "Car not found."}
            socket.send_json(response)

if __name__ == "__main__":
    main()
