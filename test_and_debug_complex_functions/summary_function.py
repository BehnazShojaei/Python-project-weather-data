from weather import *

example_one = [
    ["2021-07-02T07:00:00+08:00", 49, 67],
    ["2021-07-03T07:00:00+08:00", 57, 68],
    ["2021-07-04T07:00:00+08:00", 56, 62],
    ["2021-07-05T07:00:00+08:00", 55, 61],
    ["2021-07-06T07:00:00+08:00", 53, 62]
    ]
example_two = [
    ["2020-06-19T07:00:00+08:00", 47, 46],
    ["2020-06-20T07:00:00+08:00", 51, 67],
    ["2020-06-21T07:00:00+08:00", 58, 72],
    ["2020-06-22T07:00:00+08:00", 59, 71],
    ["2020-06-23T07:00:00+08:00", 52, 71],
    ["2020-06-24T07:00:00+08:00", 52, 67],
    ["2020-06-25T07:00:00+08:00", 48, 66],
    ["2020-06-26T07:00:00+08:00", 53, 66]
    ]
example_three = [
    ["2020-06-19T07:00:00+08:00", -47, -46],
    ["2020-06-20T07:00:00+08:00", -51, 67],
    ["2020-06-21T07:00:00+08:00", 58, 72],
    ["2020-06-22T07:00:00+08:00", 59, 71],
    ["2020-06-23T07:00:00+08:00", -52, 71],
    ["2020-06-24T07:00:00+08:00", 52, 67],
    ["2020-06-25T07:00:00+08:00", -48, 66],
    ["2020-06-26T07:00:00+08:00", 53, 66]
    ]

example_four = [
    ["carrot", -47, -46],
    ["2020-06-20T07:00:00+08:00", -51, 67],
    ["2020-06-21T07:00:00+08:00", 58, 72],
    ["2020-06-22T07:00:00+08:00", 59, 71]
]

example_five = [
    
    ["2020-06-21T07:00:00+08:00","" , 72],
    ["2020-06-22T07:00:00+08:00", 59, 71]
]

def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
 
    day_list = []
    min_list = []
    max_list = []
    
    for row in weather_data:

        # Check if the row has all three elements: date, min, and max temperatures
        if len(row) < 3 or not row[0] or row[1] == '' or row[2] == '':
            # Skip rows with missing data
            continue

    
        day_list.append(row[0])
        min_list.append(convert_f_to_c(row[1]))
        max_list.append(convert_f_to_c(row[2]))
    
    number_of_days = len(weather_data) 
    
    min_temp , index_min_temp = find_min(min_list)
    max_temp , index_max_temp = find_max(max_list)

    min_temp_c = format_temperature(min_temp)
    max_temp_c = format_temperature(max_temp)

    last_day_of_min = convert_date(day_list[index_min_temp])
    last_day_of_max = convert_date(day_list[index_max_temp])

    str_of_average_low = format_temperature(calculate_mean(min_list))
    str_of_average_high = format_temperature(calculate_mean(max_list))

    summary = (f"{number_of_days} Day Overview\n"
            f"  The lowest temperature will be {min_temp_c}, and will occur on {last_day_of_min}.\n"
            f"  The highest temperature will be {max_temp_c}, and will occur on {last_day_of_max}.\n"
            f"  The average low this week is {str_of_average_low}.\n"
            f"  The average high this week is {str_of_average_high}.\n")

    print (summary)
    return summary

# generate_summary(example_one)
# generate_summary(example_two)
# generate_summary(example_three)
# generate_summary(example_four)
generate_summary(example_five)

# 5 Day Overview
#   The lowest temperature will be 9.4°C, and will occur on Friday 02 July 2021.
#   The highest temperature will be 20.0°C, and will occur on Saturday 03 July 2021.
#   The average low this week is 12.2°C.
#   The average high this week is 17.8°C.

# 8 Day Overview
#   The lowest temperature will be 8.3°C, and will occur on Friday 19 June 2020.
#   The highest temperature will be 22.2°C, and will occur on Sunday 21 June 2020.
#   The average low this week is 11.4°C.
#   The average high this week is 18.8°C.

# 8 Day Overview
#   The lowest temperature will be -46.7°C, and will occur on Tuesday 23 June 2020.
#   The highest temperature will be 22.2°C, and will occur on Sunday 21 June 2020.
#   The average low this week is -16.1°C.
#   The average high this week is 12.4°C.

    #check weather_data is a list of lists? call function load_data_from_csv
    #check how many lines we have in the data put the number in variable number_of_day and keep a big loop running until we reach to no data
    # for list_of_lists[0] call function convert_date() in return nice format of date
    #for list_of_lists[1] call function convert f to c to have celcuis then find min get min_value call format_temparature put the value in variable string_of_min get last position and put related call convert date into a variable last_day_min and calculate mean and call format_temparature put the value in variable string_of_avg_low
    #for list_of_lists[2] call function convert f to c to have celcuis then find max call format_temparature put the value in variable string_of_max get last position and put related call convert date into a variable last_day_max and calculate mean and call format_temparature put the value in variable string_of_avg_high
    # out put will be a string" {number_of_day} Day Overview"
    # "The lowest temperature will be {string_of_min}, and will occur on {last_day_of_min}."
    # "The highest temperature will be {string_of_max}, and will occur on {last_day_of_max}."
    # " The average low this week is {string_of_average_low}.""
    # "The average high this week is {string_of_avg_high}.""
