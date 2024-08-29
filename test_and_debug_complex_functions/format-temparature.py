 
# def try_float(item, raise_error=False):
#     """
#     Tries to convert the item to float.

#     Args:
#         item: The item to be converted.
#         raise_error: If True, raises ValueError on failure; otherwise, returns None.

#     Returns:
#         A float if conversion is successful, or None if not and raise_error is False.
    
#     Raises:
#         ValueError: If raise_error is True and conversion fails.
#     """
#     try:
#         return float(item)
#     except ValueError as e:
#         if raise_error:
#             raise ValueError(f"Invalid data format: {e}")
#         return None
    
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
        temp = round(float(temp),1) 
        return f"{temp}{DEGREE_SYMBOL}"   
    except ValueError:
        raise ValueError("Invalid input {temp} must be a number")

    # temp = try_float(temp, raise_error=True)
    # temp = round(temp,1)
    # return f"{temp}{DEGREE_SYMBOL}"


temp1 = 20
temp2 = -12
temp3 = "3"
temp4 = "carrot"
temp5 =""

format_temperature(temp1)