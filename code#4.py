prin_amu = float(input("Enter the loan amount: "))
annual_interest_rate = float(input("Enter the annual interest rate (%): "))
months = float(input("Enter the loan tenure in months: "))


# Interest per month
r = annual_interest_rate/(12*100)

emi = prin_amu * r * ((1+r)**months)/((1+r)**months - 1)

print("Monthly EMI is",emi,"/-")