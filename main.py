#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

print("Hello, this is a Felipe's project. This is a tip calculator for you to use whenever you need!")

# Getting the bill and already converting it as a floating point number.
total_bill = float( input("What is the total bill? $"))

# Get the tip percentage. Calculate the increase factor. E.g: The bill is 150 and the tip percentage is 12, the increase factor will be 1.12 (1 + (12 / 100) and the final bill will be 150 * 1.12 = 168.0.
tip_percentage =float( input("How much tip would you like to give? 10, 12 or 15? "))
increase_factor_float = 1 + tip_percentage / 100
bill_plus_tip = round(total_bill * increase_factor_float, 1)

# How many people will split the bill with you? Divide the bill by the amount of people that are going to pay. Then you have the final bill per person!
people_to_split = int( input("How many people will pay the bill? "))
final_bill_per_person = round(bill_plus_tip / people_to_split, 2)

print(f"Each person should pay: ${final_bill_per_person}")
