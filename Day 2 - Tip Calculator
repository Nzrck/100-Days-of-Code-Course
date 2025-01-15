print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

#short form
bill_share = round(((bill + bill * (tip / 100)) / people), 2)
print(f"Each person should pay: ${bill_share:.2f}")

#long form, broken down
tip_amount = bill * (tip / 100)
bill_and_tip = bill + tip_amount
share_per_person = round((bill_and_tip / people),2)
final_amount = "{:.2f}".format(share_per_person)
print(f"Each person should pay: ${final_amount}")
