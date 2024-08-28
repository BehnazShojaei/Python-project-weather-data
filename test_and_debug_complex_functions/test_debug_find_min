def try_float(item, raise_error=False):
    """
    Tries to convert the item to float.

    Args:
        item: The item to be converted.
        raise_error: If True, raises ValueError on failure; otherwise, returns None.

    Returns:
        A float if conversion is successful, or None if not and raise_error is False.
    
    Raises:
        ValueError: If raise_error is True and conversion fails.
    """
    try:
        return float(item)
    except ValueError as e:
        if raise_error:
            raise ValueError(f"Invalid data format: {e}")
        return None
    
def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minimum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    # Filter empty strings or non-convertible elements like "carrot" and replace it with None to keep indexing untouched! 

    weather_data = [try_float(item) for item in weather_data]
    # List comprehension to exclude None values
    valid_data = [item for item in weather_data if item is not None]
    print(valid_data)

    if not valid_data:  # If all values are None, or the list is empty return empty tuple
        return ()

    min_value = min(valid_data)
    
    reversed_list = weather_data[::-1] #use weather_data to have correct index
    print(reversed_list)
    last_position = len(weather_data) - 1 - reversed_list.index(min_value)

    print(min_value , last_position)
    return (min_value , last_position)

temperatures1 = [49, 57, 56, 55, 53]
temperatures2 = [-10, -8, 2, -16, 4]
temperatures3 = [10.4, 14.5, 12.9, 8.9, 10.5, 11.7]
temperatures4 = ["49", "57", "56", "55", "53", "49"]
temperatures5 = []
temperatures6 = [49, 57, 56, 55, 53, 49]
temperatures7 = [49, "57", 56, 55,0 ,0, 53, "0", "carrot", ""]

find_min(temperatures7)
