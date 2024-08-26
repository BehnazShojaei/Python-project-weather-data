
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

    try:
        weather_data = [float(item) for item in weather_data]
        if len(weather_data) == 0:
            raise ValueError("The list is empty.")
        mean_value = sum(weather_data) / len(weather_data)
        print (mean_value)
        return mean_value
    except ValueError as error:
        raise ValueError(f"Invalid input: {error}")

#  def test_calculate_mean(self):
#         temperatures = [49, 57, 56, 55, 53]
#         expected_result = 54
#         result = weather.calculate_mean(temperatures)
#         self.assertEqual(result, expected_result)

#     def test_calculate_mean_floats(self):
#         temperatures = [51.0, 58.2, 59.9, 52.4, 52.1, 48.4, 47.8, 53.43]
#         expected_result = 52.90375
#         result = weather.calculate_mean(temperatures)
#         self.assertEqual(result, expected_result)

#     def test_calculate_mean_strings(self):
#         temperatures = ["51", "58", "59", "52", "52", "48", "47", "53"]
#         expected_result = 52.5
#         result = weather.calculate_mean(temperatures)
#         self.assertEqual(result, expected_result)
    
#     def test_calculate_mean_negative(self):
#         temperatures = [-51, -58, -59, -52, -52, -48, -47, -53]
#         expected_result = -52.5
#         result = weather.calculate_mean(temperatures)
#         self.assertEqual(result, expected_result)


# weather_data = [49, 57, 56, 55, 53]
# weather_data = [51.0, 58.2, 59.9, 52.4, 52.1, 48.4, 47.8, 53.43]
# weather_data = ["51", "58", "59", "52", "52", "48", "47", "53"]
# weather_data = [-51, -58, -59, -52, -52, -48, -47, -53]
weather_data = ["carrot", 3 , 4]
# weather_data = ["51", 31 , "-3", 5.2]
# weather_data = []
calculate_mean(weather_data)
