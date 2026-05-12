#Defined functions area
def calculate_average_speed(distance_km, time_hours):
    return distance_km / time_hours

def calculate_pace(time_minutes, distance_km):
    return time_minutes / distance_km

def calculate_estimated_calories(time_hours, calories_per_hour):
    return time_hours * calories_per_hour

def calculate_target_time_hours(distance_km, target_speed_kmh):
    target_time_hours = distance_km / target_speed_kmh
    return target_time_hours * 60

#User input area
print("Enter bike ride details below")
print()
distance_km = float(input("Enter distance in km: "))
time_minutes = float(input("Enter time in minutes: "))
target_speed_kmh = float(input("Enter target speed in km/h: "))
calories_per_hour = float(input("Enter estimated calories burned per hour: "))
print()

if distance_km <= 0 or time_minutes <= 0 or target_speed_kmh <= 0 or calories_per_hour <= 0:
    print("Error: distance, time, target speed and calories must all be greater than 0.")

#user calculation area
else:
    time_hours = time_minutes / 60
    average_speed = calculate_average_speed(distance_km, time_hours)
    estimated_calories = calculate_estimated_calories(time_hours, calories_per_hour)
    pace_minutes_per_km = calculate_pace(time_minutes, distance_km)
    target_time_minutes = calculate_target_time_hours (distance_km, target_speed_kmh)

    time_difference = time_minutes - target_time_minutes
    speed_difference = average_speed - target_speed_kmh
    ride_seconds = time_minutes * 60

    energy_joules = estimated_calories * 4184
    efficiency = 0.24
    mechanical_energy = energy_joules * efficiency
    estimated_watts = mechanical_energy / ride_seconds

    #Ride rating area
    if average_speed < 20:
        ride_rating = "Easy pace"
    elif average_speed < 27:
        ride_rating = "Medium pace"
    elif average_speed < 32:
        ride_rating = "Strong pace"
    else:
        ride_rating = "Fast pace"

 #Ride wattage area
    if estimated_watts <100:
        wattage_rating = "Very Easy"
    elif estimated_watts < 180:
        wattage_rating = "Endurance ride"
    elif estimated_watts < 250:
        wattage_rating = "Strong ride"
    else:
        wattage_rating = "Hard effort"

    #Ride recommendation area
    if time_difference > 10:
        recommendation = "You missed your target by alot. Lower the target speed or build more endurance"
    elif time_difference > 0:
        recommendation = "You were close to your target. Try the same route again and pace more evenly"
    elif time_difference < -10:
        recommendation = "You beat your target by alot. Try increasing your speed next ride"
    elif time_difference < 0:
        recommendation = "Good ride. You slightly beat your goal"
    else:
        recommendation = "Perfect pacing. Try extending the distance next ride"


#Print calculations area
    print("--- Ride Summary ---")
    print("You rode", distance_km, "km in", time_minutes, "minutes")
    print()
    print("--- Performance area ---")
    print("Average speed:", round(average_speed, 1), "km/h")
    print("Pace per kilometre:", round(pace_minutes_per_km, 2), "minutes per kilometre")
    print("Estimated average wattage:", round(estimated_watts, 1), "watts")
    print("Estimated Calories:", round(estimated_calories), "calories")
    print("Ride Rating:", ride_rating)
    print("Ride type:", wattage_rating)
    print()
    print("--- Target area ---")
    print("Estimated time at target speed:", round(target_time_minutes, 1), "minutes")
    print("Time difference from target:", round(time_difference, 1), "minutes")
    print("Speed difference from target:", round(speed_difference, 1), "km/h")
    print()
    print("--- Recommendations ---")
    print("Recommendation: ", recommendation)
    print()


#target time message area
    if time_difference > 0:
        print ("You missed your target by", round(time_difference, 1), "minutes.")
    elif time_difference < 0:
        print ("You beat your target by", round(time_difference * -1, 1), "minutes." )
    else:
        print ("You matched your target time.")

#target speed area
    if speed_difference > 0:
        print ("You were", round(speed_difference, 1), "km/h above your target speed.")
    elif speed_difference < 0:
        print ("You were", round(speed_difference * -1, 1), "km/h below your target speed.")
    else:
        print ("You matched your target speed exactly.")