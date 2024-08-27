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
        temp = float(temp)
        return f"{temp}{DEGREE_SYMBOL}"   
    except ValueError:
        raise ValueError("Invalid input {temp} must be a number")


    
def convert_date(iso_string):
    """Converts and ISO formatted date into a human-readable format.

    Args:
        iso_string: An ISO date string.
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    try:
        date_object = datetime.fromisoformat(iso_string) # Parse ISO format date string to datetime object
        return date_object.strftime("%A %d %B %Y")
    except ValueError:
        raise ValueError("The provided date must be in ISO format (YYYY-MM-DD).")


def convert_f_to_c(temp_in_fahrenheit):
    """Converts a temperature from Fahrenheit to Celcius.

    Args:
        temp_in_fahrenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees Celcius, rounded to 1 decimal place.
    """   
    try:
        temp_in_f = float(temp_in_fahrenheit)
        temp_in_c = (temp_in_f - 32) * 5 / 9 # Convert Fahrenheit to Celsius
        return round(temp_in_c, 1) # Round to 1 decimal place
    except ValueError:
        raise ValueError(f"Invalid input {temp_in_fahrenheit}. It should be a float number.")
    


def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    # the code will check if the list is empty, if it is convertible to float, if it's not then we will get detailed msg of error
    try:
        weather_data = [float(item) for item in weather_data]
        if len(weather_data) == 0: 
            raise ValueError("The list is empty.")
        mean_value = sum(weather_data) / len(weather_data)
        return mean_value
    except ValueError as error:
        raise ValueError(f"Invalid input: {error}")


def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.
    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """

    data_list = [] #an empty list to store data
    try:
        with open(csv_file, mode='r', newline='', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file) #using dict to be readable
            
            for row in csv_reader:
                try:
                    date = row["date"]
                    min_temp = float(row["min"])
                    max_temp = float(row["max"])
                    data_list.append([date, min_temp, max_temp]) #each row will be a sublist of the data list
                
                except KeyError: #if there is a missing column
                    raise ValueError("Missing required columns in the CSV file.")
                except ValueError as e: #if we can't convert to float
                    raise ValueError(f"Invalid data format: {e}")
    
    except FileNotFoundError: #if there is no file
        raise FileNotFoundError(f"The file at {csv_file} does not exist.")
    except Exception as e: #any other error 
        raise Exception(f"An error occurred while reading the CSV file: {e}")

    return data_list


def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minimum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    if not weather_data:  # Check if the list is empty
        return ()

    # Filter out empty strings or non-convertible elements like "carrot"
    cleaned_data = []
    for item in weather_data:
        try:
            cleaned_data.append(float(item))  # Convert each item to float
        except ValueError:
            # Skip any element that can't be converted to float
            continue

    if not cleaned_data:  # Check if all lines were empty or non-convertible
        return ()

    min_value = cleaned_data[0]  # Initialize min value
    min_index = 0  # Initialize min index

    for index in range(len(cleaned_data)):  # Find the last occurrence of the minimum
        if cleaned_data[index] <= min_value:
            min_value = cleaned_data[index]
            min_index = index

    return min_value, min_index


def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    if not weather_data:  
        return ()

    cleaned_data = []
    for item in weather_data:
        try:
            cleaned_data.append(float(item))  
        except ValueError:
            continue

    if not cleaned_data:  
        return ()

    max_value = cleaned_data[0]  
    max_index = 0  

    for index in range(len(cleaned_data)):  
        if cleaned_data[index] >= max_value:
            max_value = cleaned_data[index]
            max_index = index

    return max_value, max_index



def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """

    for row in weather_data:
        # Check if the row has all three elements: date, min, and max temperatures
        if len(row) < 3 or not row[0] or row[1] == '' or row[2] == '':
            # Skip rows with missing data
            continue

    day_list = []
    min_list = []
    max_list = []

    for row in weather_data:
        day_list.append(row[0])
        min_list.append(convert_f_to_c(row[1]))  # convert_f_to_c and all other functions handles its own errors
        max_list.append(convert_f_to_c(row[2]))  

    number_of_days = len(weather_data)

    if not min_list or not max_list:
        return "No valid temperature data available."

    min_temp, index_min_temp = find_min(min_list)
    max_temp, index_max_temp = find_max(max_list)

    min_temp_c = format_temperature(min_temp)
    max_temp_c = format_temperature(max_temp)

    last_day_of_min = convert_date(day_list[index_min_temp])
    last_day_of_max = convert_date(day_list[index_max_temp])

    str_of_average_low = format_temperature(round(calculate_mean(min_list),1))
    str_of_average_high = format_temperature(round(calculate_mean(max_list),1))

# I wanted to avoid calling convert_f_to_c multiple times so I applied when streaming from data, but while calculating the mean of multiple float end up having more than 1 decimal f now I need to apply round two times! 
    
    summary = (f"{number_of_days} Day Overview\n"
            f"  The lowest temperature will be {min_temp_c}, and will occur on {last_day_of_min}.\n"
            f"  The highest temperature will be {max_temp_c}, and will occur on {last_day_of_max}.\n"
            f"  The average low this week is {str_of_average_low}.\n"
            f"  The average high this week is {str_of_average_high}.\n")
    
    return summary

def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    daily_summary= ""
    for row in weather_data: # Skip empty rows or rows with missing data
        if not row or len(row) < 3 or row[0] == '' or row[1] == '' or row[2] == '':
            continue

        date = convert_date(row[0])
        min_temp_c = format_temperature(convert_f_to_c(row[1]))
        max_temp_c = format_temperature(convert_f_to_c(row[2]))
    
        daily_summary += (f"---- {date} ----\n"
                        f"  Minimum Temperature: {min_temp_c}\n"
                        f"  Maximum Temperature: {max_temp_c}\n\n")
    
    return daily_summary


################??????????????????????Question for daily summary or summary how to handle missing column I handled by skipping that day is it the best way?