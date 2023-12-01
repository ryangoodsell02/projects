# tipping calculator

print("Welcome to the tip calculator.")


# input
total_bill = float(input("\nWhat was the total bill? $"))
perc_tip = int(input("\nWhat is the percentage that you want to tip? Choose 10, 12, or 15. "))
num_people = int(input("\nHow may people should split the bill? "))


# processing

new_perc_tip = perc_tip / 100
split_bill = (total_bill + (total_bill * new_perc_tip)) / num_people




# output


print(f"\nEach person should pay: ${round(split_bill, 2)}")

