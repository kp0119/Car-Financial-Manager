import zmq

def calculate_budget(yearly_income):
    budget = yearly_income * 0.20
    return {
        'car_budget': round(budget, 2)
    }

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5558")

print("Car Budget Calculator Microservice is running...")

while True:
    message = socket.recv_json()
    action = message.get('action')

    if action == 'calculate_budget':
        yearly_income = message.get('yearly_income')
        if yearly_income is None:
            response = {"error": "Missing 'yearly_income' parameter"}
        else:
            try:
                yearly_income = float(yearly_income)
                response = calculate_budget(yearly_income)
            except ValueError:
                response = {"error": "Invalid 'yearly_income' value"}

    else:
        response = {"error": "Invalid action"}

    socket.send_json(response)
