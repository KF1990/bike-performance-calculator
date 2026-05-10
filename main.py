#User input area
distance_km = float(input("Enter distance in km: "))
time_minutes = float(input("Enter time in minutes: "))
target_speed_kmh = float(input("Enter target speed in km/h: "))
calories_per_hour = float(input("Enter estimated calories burned per hour: "))

if distance_km <= 0 or time_minutes <= 0 or target_speed_kmh <= 0 or calories_per_hour <= 0:
    print("Error: distance, time, target speed and calories must all be greater than 0.")

#user calculation area
else:
    time_hours = time_minutes / 60
    average_speed = distance_km / time_hours
    estimated_calories = time_hours * calories_per_hour
    pace_minutes_per_km = time_minutes / distance_km

    target_time_hours = distance_km / target_speed_kmh
    target_time_minutes = target_time_hours * 60
    time_difference = time_minutes - target_time_minutes
    if average_speed < 20:
        ride_rating = "Easy pace"
    elif average_speed < 27:
        ride_rating = "Medium pace"
    elif average_speed < 32:
        ride_rating = "Strong pace"
    else:
        ride_rating = "Fast pace"
    print()
    print("--- Ride Summary ---")
    print("You rode", distance_km, "km in", time_minutes, "minutes")

#Print calculations area
    print("Average speed:", round(average_speed, 1), "km/h")
    print("Estimated time at target speed:", round(target_time_minutes, 1), "minutes")
    print("Pace per kilometre:", round(pace_minutes_per_km, 2), "minutes per kilometre")
    print("Time difference from target:", round(time_difference, 1), "minutes")
    print("Estimated Calories:", round(estimated_calories), "calories")
    print("Ride Rating:", ride_rating)


    if time_difference > 0:
        print ("You missed your target by", round(time_difference, 1), "minutes")
    elif time_difference < 0:
        print ("You beat your target by", round(time_difference * -1, 1), "minutes" )
    else:
        print ("You matched your target speed")