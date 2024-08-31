
def try_float(item, raise_error=False): #this function will check our item and try to make it a float number where possible return None for non convertible, Filter empty strings or non-convertible elements like "carrot" while keep the indexing same  
    try:
        return float(item)
    except ValueError as e:
        if raise_error:
            raise ValueError(f"Invalid data format: {e}")
        return None

def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    
    # try:
    #     weather_data = [float(item) for item in weather_data]
    # except ValueError:
    #     print(f"Invalid input weather_data should be a list of float numbers")
    #     return None
    # mean_value = sum(weather_data)/ len(weather_data) 
    # print (mean_value)
    # return mean_value

    

    # try:
    #     weather_data = [float(item) for item in weather_data]
    # except ValueError:
    #     raise ValueError ("Invalid input weather_data should be a list of float numbers")
    # if len(weather_data) == 0:
    #     raise ValueError("The list is empty.")
    # mean_value = sum(weather_data)/ len(weather_data) 
    # print (mean_value)
    # return mean_value

    # weather_data = [try_float(item) for item in weather_data]
    # print(weather_data)
    # if len(weather_data) == 0:
    #     raise ValueError("The list is empty.")
    # mean_value = sum(weather_data) / len(weather_data)
    # print (mean_value)
    # return mean_value

    weather_data = [try_float(item) for item in weather_data]
    # List comprehension to exclude None values
    valid_data = [item for item in weather_data if item is not None]
    print(valid_data)

    if not valid_data:  # If all values are None, or the list is empty return empty tuple 
        return ()
    mean_value = sum(valid_data) / len(valid_data)
    print (mean_value)
    return mean_value

weather_data1 = [49, 57, 56, 55, 53]
weather_data2 = [51.0, 58.2, 59.9, 52.4, 52.1, 48.4, 47.8, 53.43]
weather_data3 = ["51", "58", "59", "52", "52", "48", "47", "53"]
weather_data4 = [-51, -58, -59, -52, -52, -48, -47, -53]
weather_data5 = ["carrot", 3 , 4]
weather_data6 = ["51", 31 , "-3", 5.2]
weather_data7 = []
print(calculate_mean(weather_data7))
