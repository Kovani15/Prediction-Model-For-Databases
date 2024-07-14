Order Prediction System
This Python script allows you to predict the next order date, the average quantity of products, and the total value of the next order for
a selected customer based on historical order data from a CSV file.

-Features
Load order data from a CSV file.
Predict the next order date for a selected customer.
Predict the average quantity of products for the next order.
Calculate the total value of the next order.
Interactive prompts to choose between making another prediction, using the same data, loading a new data source, or exiting the program.


-Requirements
Python 3.x
pandas
tkinter


-Install the required Python packages:
pip install pandas (you can open the install panda.bat file for this)

-Usage
Ensure your CSV file (ordenes.csv) is correctly formatted:

-Run the script:
Prediction System.bat

-Follow the interactive prompts:
Select the CSV file: A dialog will appear to select your CSV file.

Enter the Customer ID: Type the ID of the customer you want to predict the next order for.

Choose the next action:
1 - Make another prediction
2 - Exit

If choosing to make another prediction, decide whether to:
1 - Use the same data
2 - Load a new data source

Notes
Ensure your dates in the CSV file are in the MM/DD/YYYY format.
The script assumes that the quantity column contains integer values.
The total value of the next order is calculated as twice the average quantity.

Packages used:
-pandas: A powerful data manipulation and analysis library.
-datetime: A module for manipulating dates and times.
-tkinter: A standard GUI library for Python, used here to create a file dialog for selecting the CSV file.
