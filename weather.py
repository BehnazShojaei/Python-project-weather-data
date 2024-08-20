import csv
from datetime import datetime

DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and Celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees Celcius."
    """
    try:
        temp = float(input(temp))
        return f"{temp}{DEGREE_SYMBOL}"   
    except ValueError:
        print(f"Invalid input {temp} should be a number")
        return None


    
def convert_date(iso_string):
    """Converts and ISO formatted date into a human-readable format.

    Args:
        iso_string: An ISO date string.
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    try:
        date_obj = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S%z")
        return date_obj.strftime("%A %d %B %Y") 
    except ValueError:
        print(f"Invalid input {iso_string} should be a in 'yyyy-mm-ddThh:mm:ss+zz:zz' format")
        return None



def convert_f_to_c(temp_in_fahrenheit):
    """Converts a temperature from Fahrenheit to Celcius.

    Args:
        temp_in_fahrenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees Celcius, rounded to 1 decimal place.
    """

    try:
        return round((float(temp_in_fahrenheit) - 32)* 5/9 , 1)
    
    except ValueError:
        print(f"Invalid input {temp_in_fahrenheit} should be a float number")
        return None
    


def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    
    try:
        weather_data = [float(item) for item in weather_data]
    except ValueError:
        print(f"Invalid input weather_data should be a list of float numbers")
        return None
    mean_value = sum(weather_data)/ len(weather_data) 
    return mean_value




def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.
    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    csv_list_of_lists =[]
    with open (csv_file, mode='r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for line in csv_reader:
            if line: #check line is not empty
                for i in range(1, len(line)): #check each item in line is int
                    try:
                        line[i] = float(line[i]) #consider both int and float at the same time, I can seperate check int and float! is there any point?
                    except ValueError:
                        pass #leave it as string if it can't be converted
                csv_list_of_lists.append(line)
                print(csv_list_of_lists)
        return csv_list_of_lists
    


def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minimum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    if not weather_data: #check if the list is not empty
        return () 

    try: 
        weather_data = [float(item) for item in weather_data] #check if the list item can be float   
    except ValueError:     
        return ()
        
    reversed_list = weather_data[::-1]
    min_value = min(reversed_list)
    last_position = len(weather_data) - 1 - reversed_list.index(min_value)

    return (min_value , last_position)


def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    pass


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass
