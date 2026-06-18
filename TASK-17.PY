#17 Write a Python program to calculate simple interest and total amount payable.
principal = float(input("Enter principal: "))
rate = float(input("Enter rate: "))
time = float(input("Enter time: "))

interest = (principal * rate * time) / 100
total = principal + interest

print("Interest:", interest)
print("Total Payable:", total)
