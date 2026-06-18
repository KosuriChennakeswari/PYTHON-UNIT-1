#12 Write a Python program to calculate the Body Mass Index (BMI) using weight and height. 

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height ** 2)

print("Your BMI is:", round(bmi, 2))
