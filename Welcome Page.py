import subprocess

print("Welcome Screen:")
print("Welcome to Karans Auto Affordability Calculator")
print("In this application you are able to get an estimated monthly payment for a potential car purchase.")
print("By using our monthly loan payment feature you wil be able to understand the financial commitment to that "
      "vehicle.")
user_input = input("Type 2 to continue to the home page: ")

if user_input == "2":
    subprocess.run(["python", "Home Page.py"])




