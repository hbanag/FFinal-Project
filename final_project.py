import seaborn as sns
import pandas as pd
import datetime #Provide source
import json
import argparse
import matplotlib.pyplot as plt


class Car:
    """
    Inializes a Car instance with attributes for make, model, year, mileage, condition, and base value

    Attributes:
        make (str): The make of the car
        model (str): The model of the car
        year (int): The year of production
        mileage (int): The mileage of the car in miles
        condition (str): The condition of the car ("New", "Used", or "Salvage") - capitlize-sensitve
        base_value (float): The initial bought cost of the car in dolars

    """
    def __init__(self, make = "Unknown", model = "Unknown", year = None, mileage = 0, condition = "Used", base_value = 20000):
        """
            Inializes a Car instance with attributes for make, model, year, mileage, condition, and base value

        Args:
            make (str): The make of the car
            model (str): The model of the car
            year (int): The year of production
            mileage (int): The mileage of the car in miles
            condition (str): The condition of the car ("New", "Used", or "Salvage") - capitlize-sensitve
            base_value (float): The initial bought cost of the car in dolars

        Raises:
            ValueError: 
                'year' is in the future
                'mileage' is negative
                'condition' is invalid

        Side effects:
            Calls 'validate_inputs' to ensure all attributes are valid and working

        """
        
        self.make = make
        self.model = model
        self.year = year if year else datetime.datetime.now().year #Provide source
        self.mileage = mileage
        self.condition = condition # Explain this
        self.base_value = base_value  # Allow base value input
        self.validate_inputs()

    def validate_inputs(self):
        """
        This validates the attributes of the Car instance

        We will be subtracting depreaition based on age and mileage

        conditon
            -'New': 1.2 (this illustrates a 20% increase to the value)
            -'Used': 0.8 (this illustrates a 20% decrease to the value)
            -'Salvage': 0.5 (this illustrates a 50% decrease)


        Raises:
            ValueError:
                'year' is in the future
                'mileage' is negative
                'condition' is invalid
        
        Side effects:
            Modifies the the state of the Car instance 
        """
        current_year = datetime.datetime.now().year
        if self.year > current_year:
            raise ValueError(f"Year of production cannot be in the future: {self.year}")
        if self.mileage < 0:
            raise ValueError(f"Mileage cannot be negative: {self.mileage}")
        if self.condition not in ["New", "Used", "Salvage"] :
            raise ValueError(f"Invalid condition: {self.condition}")
    
    def calculate_value(self):
        """
        This calcualtes the estiamted value of the car



        Returns:
            car_value (float): The estimated value of the car

        Side effects:
            It does not modify the attributes of the Car instance
        
        """
        
        current_year = datetime.datetime.now().year
        age = current_year - self.year
        base_value = 20000 # explain this part

        age_depr = max(0, self.base_value - (age * 1000))

        mileage_factor = max(0, age_depr - (self.mileage / 100)) # explain this part

        car_condition = { #Explain the use of these specific floats
            "New": 1.2,
            "Used": 0.8,
            "Salvage": 0.5
        }

        car_condition = car_condition[self.condition]

        car_value = mileage_factor * car_condition

        return max(car_value, 0)
    
    def __str__(self):
        """
        This then returns a formatted string representation of the Car instance

        Returns: 
            str: A string describing the car's make, model, year, mileage, and condiiton

        Side effects:
            Error will occur if input is invaid
        """

        return f"{self.make} {self.model} ({self.year}), {self.mileage} miles, Condition: {self.condition}"

def depr_graph(year, base_value, condition):
    """
    This plots a line graph showing the depreation of the car's value over time

    Args:
        year (int): The year of production for the car.
        base_value (float): The initial value of the car in dollars.
        condition (str): The condition of the car ("New", "Used", or "Salvage").

    Raises:
        KeyError: If the provided condition is not one of "New", "Used", or "Salvage".

    Side Effects:
        Displays a line plot using Seaborn and Matplotlib.
        Rotates x-axis labels for better readability.

    """

    current_year = datetime.datetime.now().year
    years = list(range(year, current_year + 1))

    condition_factors = {
        "New": 1.2,
        "Used": 0.8,
        "Salvage": 0.5
    }
    condition_factor = condition_factors[condition]

    values = []
    for y in years:
        age = y - year
        value = base_value * condition_factor * (0.85 ** age)  # 15% annual depreciation
        values.append(max(value, 0))


    data = pd.DataFrame({"Year": years, "Value": values})

    sns.set_theme() #provide link from ELMS Module
    ax = sns.lineplot(
        data = data, x = "Year", y = "Value", marker= 'o'
    )

    ax.set_title("Car Value Depreciation Over Time")
    ax.set_xlabel("Year")
    ax.set_ylabel("Estimated Value ($)")

    ax.set_xticks(years)  # Ensure all years are shown as ticks
    ax.set_xticklabels([str(y) for y in years], rotation=45) 

    plt.show()

if __name__ == "__main__":
    """
    This script interacts with the user to gain data on their car, 
    calculates theestimated value using the 'Car' class, and illustrates a line plot 
    
    Args (User Input):
        make (str): The make of the car 
        model (str): The model of the car
        year (int): The year of production for the car.
        mileage (int): The car's mileage in miles.
        condition (str): The condition of the car ("New", "Used", "Salvage").
        base_value (int): The car's base value in dollars.
    
    Raises:
        ValueError: If invalid input is provided for:
            `year` (in the future)
            `mileage` (negative numbers)
            `condition` (does not input specifically 'New', 'used', 'Salvage')
    
    Side Effects:
        Prints the car's estimated value and description of the car.
        Illustrates a depreciation graph using Seaborn and Matplotlib.
    """

    print("Do you know how much your car is worth?")

    try:
        make = input("Enter the make of the car (ex. Honda, Audi): ")
        model = input("Enter the model of the car (ex. Civic, A4): ")
        year = int(input("Enter the year of production: "))
        mileage = int(input("Enter the mileage (in miles): "))
        condition = input("Enter the condition of the car (New, Used, Salvage): ")
        base_value = int(input("Enter the base value of the car (in dollars, e.g., 20000): "))

        car = Car(make, model, year, mileage, condition, base_value)

        value = car.calculate_value()
        print(f"\nThe estimated value of the car is: ${value:.2f}")
        print(f"Car Description: {car}")

        depr_graph(year, base_value, condition)

    except ValueError as e:
        print(f"Error: {e}")