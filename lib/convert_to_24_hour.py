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

