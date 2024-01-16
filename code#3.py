principal = float(input("\nEnter the Principal Amount : "))
rate = float(input("\nEnter the Annual Interest Rate (%) : ")) / 100
time = float(input("\nEnter the Time Period in years : "))


# S.I
simple_interest = (principal*rate*time)/100
print("\nThe Simple Interest on the Amount is :", simple_interest)

# C.I
frequency = int(input("\nEnter the Compounding Frequency per year : "))
amount = principal * (1 + rate / frequency) ** (frequency * time)
compound_interest = amount - principal
print("\nThe Compound Interest on the Amound is :",compound_interest,"/-")