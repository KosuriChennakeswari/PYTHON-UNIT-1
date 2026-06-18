#20 Write a Python program to estimate fuel cost based on travel distance,mileage, and fuel price. 

distance = float(input("Enter Travel Distance (km): "))

mileage = float(input("Enter Mileage (km/liter): "))

price = float(input("Enter Fuel Price per Liter: "))

fuel = distance / mileage

cost = fuel * price

print("Fuel Required =", fuel, "liters")
print("Fuel Cost = Rs.", cost)"""
