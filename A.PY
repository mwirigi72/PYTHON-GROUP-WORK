
import numpy as np

# Step 1: Store 24 hourly temperature readings
temperatures = np.array([
    18.5, 18.0, 17.8, 17.5,
    17.9, 19.0, 21.5, 23.8,
    25.6, 27.1, 28.3, 29.0,
    29.4, 31.2, 32.5, 31.8,
    28.5, 27.6, 26.2, 24.8,
    23.4, 22.1, 21.0, 19.0
])

# Step 2: Calculate temperature statistics
average = np.mean(temperatures)
minimum = np.min(temperatures)
maximum = np.max(temperatures)

# Step 3: Convert Celsius to Fahrenheit
fahrenheit = (temperatures * 1.8) + 32

# Step 4: Identify temperatures above 30 degrees
hot_readings = temperatures[temperatures > 30]

# Step 5: Display results
print("WEATHER STATION REPORT")
print("----------------------")

print(f"Average temperature: {average:.2f} °C")
print(f"Minimum temperature: {minimum:.2f} °C")
print(f"Maximum temperature: {maximum:.2f} °C")

print("\nTemperatures in Fahrenheit:")
print(fahrenheit)

print("\nReadings above 30°C:")
print(hot_readings)

print(f"\nNumber of hot readings: {len(hot_readings)}")
