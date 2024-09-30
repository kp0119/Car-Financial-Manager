import zmq

def get_instructions():
    return ("To calculate a monthly payment for a vehicle, you must first enter the information for that vehicle and loan.\n"
            "To do that, go to the home screen and select the first option.\n"
            "After selecting that option, you are given an ID for that information.\n"
            "You can then go to the calculator by pressing 3 at the end of the page.\n"
            "From the calculator, you can provide the nickname or ID of the car and it will provide you the monthly payment.\n"
            "If you entered the wrong price for the car or any other information, you can go to the 'View this vehicle's information' page.\n"
            "From here, you can view the information, update it, or delete the entry entirely.\n")

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5557")

print("Help Page Microservice is running...")

while True:
    message = socket.recv_json()
    if message['action'] == 'get_instructions':
        instructions = get_instructions()
        socket.send_json({"instructions": instructions})
