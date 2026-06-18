# Enter Loan Amount
P = float(input("Enter Loan Amount: "))

# Enter Annual Interest Rate
R = float(input("Enter Annual Interest Rate (%): "))

# Enter Repayment Duration in Months
N = int(input("Enter Repayment Duration (Months): "))

# Convert annual interest rate to monthly interest rate
R = R / (12 * 100)

# Calculate EMI
EMI = (P * R * (1 + R) ** N) / ((1 + R) ** N - 1)

print("EMI =", EMI)
