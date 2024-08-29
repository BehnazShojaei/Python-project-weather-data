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
def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    daily_summary= ""
    for row in weather_data:
        # if not row  or len(row) < 3: 
            #check if the list is not empty or any data missing
        if not row or len(row) < 3 or row[0] == '' or row[1] == '' or row[2] == '':
            continue
    
        date = convert_date(row[0])
        min_temp_c = format_temperature(convert_f_to_c(row[1]))
        max_temp_c = format_temperature(convert_f_to_c(row[2]))
    
        daily_summary += (f"---- {date} ----\n"
                        f"  Minimum Temperature: {min_temp_c}\n"
                        f"  Maximum Temperature: {max_temp_c}\n\n")
    
    print (daily_summary)
    return daily_summary
        

generate_daily_summary(example_one)
generate_daily_summary(example_two)
generate_daily_summary(example_three)

# generate_daily_summary(example_four)
generate_daily_summary(example_five)


# expected output example one

# ---- Friday 02 July 2021 ----
#   Minimum Temperature: 9.4°C
#   Maximum Temperature: 19.4°C

# ---- Saturday 03 July 2021 ----
#   Minimum Temperature: 13.9°C
#   Maximum Temperature: 20.0°C

# ---- Sunday 04 July 2021 ----
#   Minimum Temperature: 13.3°C
#   Maximum Temperature: 16.7°C

# ---- Monday 05 July 2021 ----
#   Minimum Temperature: 12.8°C
#   Maximum Temperature: 16.1°C

# ---- Tuesday 06 July 2021 ----
#   Minimum Temperature: 11.7°C
#   Maximum Temperature: 16.7°C

# expected output example two
# ---- Friday 19 June 2020 ----
#   Minimum Temperature: 8.3°C
#   Maximum Temperature: 7.8°C

# ---- Saturday 20 June 2020 ----
#   Minimum Temperature: 10.6°C
#   Maximum Temperature: 19.4°C

# ---- Sunday 21 June 2020 ----
#   Minimum Temperature: 14.4°C
#   Maximum Temperature: 22.2°C

# ---- Monday 22 June 2020 ----
#   Minimum Temperature: 15.0°C
#   Maximum Temperature: 21.7°C

# ---- Tuesday 23 June 2020 ----
#   Minimum Temperature: 11.1°C
#   Maximum Temperature: 21.7°C

# ---- Wednesday 24 June 2020 ----
#   Minimum Temperature: 11.1°C
#   Maximum Temperature: 19.4°C

# ---- Thursday 25 June 2020 ----
#   Minimum Temperature: 8.9°C
#   Maximum Temperature: 18.9°C

# ---- Friday 26 June 2020 ----
#   Minimum Temperature: 11.7°C
#   Maximum Temperature: 18.9°C


# expected output example three
# ---- Friday 19 June 2020 ----
#   Minimum Temperature: -43.9°C
#   Maximum Temperature: -43.3°C

# ---- Saturday 20 June 2020 ----
#   Minimum Temperature: -46.1°C
#   Maximum Temperature: 19.4°C

# ---- Sunday 21 June 2020 ----
#   Minimum Temperature: 14.4°C
#   Maximum Temperature: 22.2°C

# ---- Monday 22 June 2020 ----
#   Minimum Temperature: 15.0°C
#   Maximum Temperature: 21.7°C

# ---- Tuesday 23 June 2020 ----
#   Minimum Temperature: -46.7°C
#   Maximum Temperature: 21.7°C

# ---- Wednesday 24 June 2020 ----
#   Minimum Temperature: 11.1°C
#   Maximum Temperature: 19.4°C

# ---- Thursday 25 June 2020 ----
#   Minimum Temperature: -44.4°C
#   Maximum Temperature: 18.9°C

# ---- Friday 26 June 2020 ----
#   Minimum Temperature: 11.7°C
#   Maximum Temperature: 18.9°C

