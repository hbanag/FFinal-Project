## An explanation of the purpose of each file in your repository

This script calculates a car's estimated value and visualizes its depreciation over time. The Car class models attributes like make, model, year, mileage, condition, and base_value, 
with methods to validate inputs, calculate value, and display details. The depr_graph function plots depreciation trends based on age, mileage, and condition, offering realistic insights. 
Users interactively input car details, and the program computes and visualizes the results using libraries like seaborn, matplotlib, datetime, and pandas. 
This tool provides car owners an intuitive way  to estimate value and understand depreciation trends year by year.

## Clear instructions on how to run your program from the command line 
(This was created with a Mac)
To run the program from the command line, ensure Python is installed on your system along with the required libraries: seaborn, matplotlib, pandas, and datetime. 
Save the script as final_project.py in your working directory. 
Open your terminal or command prompt and navigate to the directory containing final_project.py using the cd command. 
Run the program by typing python final_project.py. 
Follow the prompts to enter car details, including the make, model, production year, mileage, condition (New, Used, or Salvage), and base value. 
The program will calculate the car’s estimated value and display a depreciation graph.

## Clear instructions on how to use your program and/or interpret the output of the program
To use the program, run it from the command line and follow the prompts. 
Enter the car’s make , model , production year , mileage in miles, condition (choose "New", "Used", or "Salvage"), and base value the user bought the car in dollars. 
The program calculates the estimated value based on these inputs and displays it, along with a detailed car description. 
Additionally, a graph visualizing the car’s depreciation over time will appear, showing the value for each year from production to the current year. 
Use the graph to understand depreciation trends.


## Annotated Bibliography

1. https://www.progressive.com/answers/what-is-car-depreciation/

2. https://www.carsdirect.com/used-car-buying/how-to-calculate-the-value-of-salvaged-vehicles

This resource provides a detailed breakdown of how car depreciation works, including the impact of a car’s condition. 
It highlights how New cars experience the fastest depreciation initially, Used cars retain more value, and Salvage cars see significant value drops due to their history of damage or accidents. 
It explains percentages that align with industry standards, such as the steep decline for salvage vehicles.

1. https://docs.python.org/3/library/datetime.html

This documentation provides an overview of the datetime module in Python, detailing its classes, functions, and methods. 
The datetime.datetime.now() function, specifically, is explained as a method to retrieve the current local date and time, which is useful for real-time applications like determining the current year

1. https://www.investopedia.com/terms/d/depreciation.asp

"value = base_value * condition_factor * (0.85 ** age) "

This explains the concept of depreciation, including its application in various industries. 
It discusses annual percentage rates like 15%, which are commonly used to estimate the decline in value of assets over time. 
The website also illustrates the mathematical framework for calculating depreciation, helping justify the usage of 0.85 ** age

1. https://matplotlib.org/stable/users/explain/axes/axes_ticks.html
2. https://stackoverflow.com/questions/10998621/rotate-axis-tick-labels

Both of these sources allowed me utlize them both to help explian 
How to customize tick labels on plots, including setting specific ticks using set_xticks() and formatting and rotating labels with set_xticklabels(). 
It is now more readable and organized (specfically, the x axis)

## Attribution

Everyone in my group dropped the class, leaving me to start and finsih the project independently
