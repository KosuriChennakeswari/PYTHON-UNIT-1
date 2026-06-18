#18 Write a Python program to calculate compound interest and maturity amount.
principal = float(input("Enter the Principal Amount: "))
rate = float(input("Enter the Rate of Interest: "))
time = float(input("Enter the Time (in years): "))

# Calculate Maturity Amount using Compound Interest formula A = P × (1 + R/100)^T
Compound Interest (CI) = A − P
amount = principal * (1 + rate / 100) ** time
compound_interest = amount - principal
print("Compound Interest =", compound_interest)
print("Maturity Amount =", amount)"""
