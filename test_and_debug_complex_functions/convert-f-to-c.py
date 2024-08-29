
def try_float(item, raise_error=False): #this function will check our item and try to make it a float number where possible return None for non convertible, Filter empty strings or non-convertible elements like "carrot" while keep the indexing same  
    try:
        return float(item)
    except ValueError as e:
        if raise_error:
            raise ValueError(f"Invalid data format: {e}")
        return None

def convert_f_to_c(temp_in_fahrenheit):
    """Converts a temperature from Fahrenheit to Celcius.

    Args:
        temp_in_fahrenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees Celcius, rounded to 1 decimal place.
    """   
    temp_in_f = try_float(temp_in_fahrenheit)
    temp_in_c = (temp_in_f - 32) * 5 / 9 # Convert Fahrenheit to Celsius
    return round(temp_in_c, 1) # Round to 1 decimal place

    # try:
    #     temp_in_f = float(temp_in_fahrenheit)
    #     temp_in_c = (temp_in_f - 32) * 5 / 9 # Convert Fahrenheit to Celsius
    #     return round(temp_in_c, 1) # Round to 1 decimal place
    # except ValueError:
    #     raise ValueError(f"Invalid input {temp_in_fahrenheit}. It should be a float number.")
    

temp_in_f1 = 64.4
temp_in_f2 = 90
temp_in_f3 = -10
temp_in_f4 = "77"
temp_in_f5 = None
temp_in_f6 = ""

print(convert_f_to_c(temp_in_f6))
# print(try_float(temp_in_f3))