# bmi


# input
print("Welcome.  We are going to check your BMI.")
weight = int(input("What is your weight in kilograms? "))
height = float(input("What is your height in meters? "))


# processing
bmi = round((weight / (height*height)), 2)
print("Your bmi is ", bmi)


# output
if bmi < 18.5:
    print("You are under weight.")
elif bmi <= 25:
    print("Your weight is normal.")
elif bmi <= 30:
    print("You are slightly overweight.")
elif bmi <= 35:
    print("You are obese.")
else:
    print("You are clinically obese")