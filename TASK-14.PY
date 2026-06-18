#14 Write a Python program to calculate the electricity bill amount based on units consumed. 

units = int(input("Enter the Number of Units Consumed: "))

# Initialize the total bill amount to 0
total = 0

# Slab 1: For the first 100 units, the rate is Rs. 5 per unit
if units <= 100:
    total = units * 5

# Slab 2: For units between 101 and 200, the rate is Rs. 7 per unit
elif units <= 200:
    # First 100 units at Rs. 5 + remaining units at Rs. 7
    total = (100 * 5) + ((units - 100) * 7)

# Slab 3: For units between 201 and 300, the rate is Rs. 10 per unit
elif units <= 300:
    # First 100 at Rs. 5 + next 100 at Rs. 7 + remaining units at Rs. 10
    total = (100 * 5) + (100 * 7) + ((units - 200) * 10)

# Slab 4: For any units consumed above 300, the rate is Rs. 15 per unit
else:
    # First 100 at Rs. 5 + next 100 at Rs. 7 + next 100 at Rs. 10 + remaining units at Rs. 15
    total = (100 * 5) + (100 * 7) + (100 * 10) + ((units - 300) * 15)

# 3. Print the final bill details
print("The Bill is Rs.", total, "for the units", units)
