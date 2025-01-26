print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

# adding tip in bill amount
final_amount = bill * (1+tip/100)
# Amount to pay by each person
each_pay = round(final_amount/people, 2)

print(f"Each person should pay: {each_pay}")
