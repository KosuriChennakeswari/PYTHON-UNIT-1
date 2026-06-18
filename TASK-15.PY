#15 Write a Python program to calculate the monthly water bill based on water consumption.

# First 1000 liters  -> Rs. 2 per liter
# Next 1000 liters   -> Rs. 3 per liter
# Above 2000 liters  -> Rs. 5 per liter

units = int(input("Enter Water Consumption (in liters): "))

bill = 0

if units <= 1000:
    # First 1000 liters
    bill = units * 2

elif units <= 2000:
    # First 1000 liters at Rs.2
    # Remaining liters at Rs.3
    bill = 1000 * 2 + (units - 1000) * 3

else:
    # First 1000 liters at Rs.2
    # Next 1000 liters at Rs.3
    # Remaining liters above 2000 at Rs.5
    bill = 1000 * 2 + 1000 * 3 + (units - 2000) * 5

print("Monthly Water Bill = Rs.", bill)
