#7 Write a Python program to convert kilometers to meters, meters to centimeters, and kilograms to grams. 

km = float(input("Enter Kilometers: "))
meters = km * 1000
print(f"{km} km = {meters} meters")

m = float(input("Enter Meters: ")) 
cm = m * 100
print(f"{m} m = {cm} centimeters")

kg = float(input("Enter Kilograms: "))
grams = kg * 1000
print(f"{kg} kg = {grams} grams")
