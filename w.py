def = AGE(current_year)

current_year = int(input("enter a year"))
age = (current_year - year_of_birth)
if age >= 2:
    print("you are " + str(age) + " years old")
elif age == "1":
    print("you are 1 year old")
elif age == "0":
    print("you will be born this very year.")
elif age == "-1":
    print("you will be born in 1 year.") 
else:
    print("you will be born in " + str(abs(age)) + " years.")