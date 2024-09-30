# Car Financial Manager CLI

**Car Financial Manager** is a Command-Line Interface (CLI) Python program that helps users manage car-related information and understand their financial commitment before purchasing a car. Users can add, view, update, or delete car details and loan information. With this information they are able to calculate monthly payments, check affordability on the vehicles, and receive recommendations on their budget for buying a car.

## Features

- **Add Car Information**: Input car details such as price, down payment, loan interest rate, and loan term.
- **View Car Information**: View, update or delete saved car and loan details.
- **Calculate Monthly Payment**: Calculate the monthly payment based on the loan terms.
- **Affordability Check**: Check if you can afford a car based on your salary and financial data.
- **Price Range Recommendation**: Get a suggestion on the price range of cars you can afford.
- **Help Section**: Get a guide on how to use the program.

## Usage

Run the program from the command line:

```bash
python Welcome Page.py
```

### Home Page Options

When proceeding to the home page you will see the following: 

```bash
Below are your options: 
1) Add Car and Loan information 
2) View Car and Loan information 
3) Monthly Payment 
4) Help 
5) What My Budget? 
6) Exit
```

- **1) Add Car and Loan information**: Add details about the car including price, down payment, interest rate, and loan term.
- **2) View Car and Loan information**: Display, update or delete saved cars and their financial information.
- **3) Monthly Payment**: Calculate the monthly loan payment for a car based on the loan amount, interest rate, and loan term. When navigating from the home page, you can see you can afford that vehicle.
- **4) Help**: Access the help section for guidance on using the program.
- **5) What My Budget?**: Determine your affordable price range for buying a car based on your financial situation.
- **6) Exit**: Exit the program.

## File Structure

- **Addcar.py**: Handles adding car and loan information.
- **affordability.py**: Manages the affordability check based on user salary and financial details.
- **budget.py**: Provides recommendations on the car price range you can afford.
- **help page.py**: Displays help information and guidance on how to navigate the program.
- **homepage.py**: The main entry point to the program, displaying options and routing to the different functionalities.
- **monthly payment page.py**: Calculates the monthly payment for a car loan.
- **view car.py**: Handles viewing stored car and loan information.
- **welcome page.py**: Displays a welcome message and introduces the program.

## Example Workflow

1. **Add Car Information**: Enter car price, down payment, interest rate, and loan term.
2. **Calculate Monthly Payment**: The program will calculate the monthly payment based on loan details.
3. **Check Affordability**: Based on your salary, the program will determine if you can afford the car.
4. **Get a Budget**: The program will suggest a price range for cars you can afford.
5. **Manage Car Records**: View, update, or delete cars from your list.

