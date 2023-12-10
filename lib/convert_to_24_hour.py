def convert_to_24_hour(hour, minute, period):
    if period == "am":
        if hour == 12:
            hour = 0
    else:  
        if hour != 12:
            hour += 12

   # Formatting hour and minute to have two digits each
    hour_str = str(hour).zfill(2)
    minute_str = str(minute).zfill(2)

 # Combining hour and minutes str
    time_24_hour = hour_str + minute_str
    print( time_24_hour)


convert_to_24_hour (12, 30, "am")
