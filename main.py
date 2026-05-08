distance_km = float(input("Enter distance in km: "))
time_minutes = float(input("Enter time in minutes: "))

time_hours = time_minutes / 60
average_speed = distance_km / time_hours

print("Average speed:", round(average_speed, 1), "km/h")