#Defined functions area
def calculate_average_speed(distance_km, time_hours):
    return distance_km / time_hours

def calculate_pace(time_minutes, distance_km):
    return time_minutes / distance_km

def calculate_estimated_calories(time_hours, calories_per_hour):
    return time_hours * calories_per_hour

def calculate_target_time_minutes(distance_km, target_speed_kmh):
    target_time_hours = distance_km / target_speed_kmh
    return target_time_hours * 60

def calculate_estimated_watts(time_minutes, estimated_calories):
    ride_seconds = time_minutes * 60
    energy_joules = estimated_calories * 4184
    efficiency = 0.24
    mechanical_energy = energy_joules * efficiency
    return mechanical_energy / ride_seconds

def get_ride_rating(average_speed):
    if average_speed < 20:
        return "Easy Ride"
    elif average_speed < 27:
        return "Medium Pace"
    elif average_speed < 32:
        return "Hard Pace"
    else:
        return "Fast Pace"

def get_wattage_rating(estimated_watts):
    if estimated_watts < 100:
        return "Very Easy"
    elif estimated_watts < 180:
        return "Endurance ride"
    elif estimated_watts < 250:
        return "Strong ride"
    else:
        return "Hard Effort"

def get_recommendation (time_difference):
    if time_difference > 10:
        return "You missed your target by alot. Lower the target speed or build more endurance"
    elif time_difference > 0:
        return "You were close to your target. Try the same route again and pace more evenly"
    elif time_difference < -10:
        return "You beat your target by alot. Try increasing your speed next ride"
    elif time_difference < 0:
        return "Good ride. You slightly beat your goal"
    else:
        return "Perfect pacing. Try extending the distance next ride"

def get_distance_category (distance_km):
    if distance_km < 20:
        return "Short ride"
    if distance_km < 30:
        return "Medium ride"
    if distance_km <50:
        return "Long ride"
    if distance_km <100:
        return "Century Ride"
    else:
        return "You are insane"

#target time message area
def get_time_target_message(time_difference):
    if time_difference > 0:
        return ("You missed your target by" + str(round(time_difference, 1)) + "minutes.")
    elif time_difference < 0:
        return ("You beat your target by" + str(round(time_difference * -1, 1)) + "minutes." )
    else:
        return ("You matched your target time.")

def get_speed_target_message(speed_difference):
    if speed_difference > 0:
        return "You were " + str(round(speed_difference, 1)) + " km/h above your target speed."
    elif speed_difference < 0:
        return "You were " + str(round(speed_difference * -1, 1)) + " km/h below your target speed."
    else:
        return "You matched your target speed exactly."

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
    target_time_minutes = calculate_target_time_minutes(distance_km, target_speed_kmh)

    time_difference = time_minutes - target_time_minutes
    speed_difference = average_speed - target_speed_kmh
    estimated_watts = calculate_estimated_watts(time_minutes, estimated_calories)

    ride_rating = get_ride_rating(average_speed)
    wattage_rating = get_wattage_rating(estimated_watts)
    recommendation = get_recommendation(time_difference)
    distance_category = get_distance_category(distance_km)
    target_time_message = get_time_target_message(time_difference)
    target_speed_message = get_speed_target_message(speed_difference)

    #Ride recommendation area


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
    print("Distance Category: ", distance_category)
    print()
    print("--- Target area ---")
    print("Estimated time at target speed:", round(target_time_minutes, 1), "minutes")
    print("Time difference from target:", round(time_difference, 1), "minutes")
    print("Speed difference from target:", round(speed_difference, 1), "km/h")
    print()
    print("--- Recommendations ---")
    print("Recommendation: ", recommendation)
    print()
    print(target_time_message)

