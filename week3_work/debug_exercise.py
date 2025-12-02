temp_water = [12, 15, 10, 5, 9]
temp_date = ["6 May 2021", "6 May 2022", "6 May 2023", "6 May 2024"]  # BUG: Only 4 dates!

# Create empty list of lists
water_measurements = []

# Loop through indices and create pairs
for i in range(len(temp_water)):  # Loops 5 times, but only 4 dates exist!
    # Create a pair [date, temperature]
    pair = [temp_date[i], temp_water[i]]
    # Add to our list of lists
    water_measurements.append(pair)

print(water_measurements) 