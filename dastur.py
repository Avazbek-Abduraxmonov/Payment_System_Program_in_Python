try:
    the_end = "the end"
    age = int(input("Enter the age "))
    if age >= 18 and age <= 86:
        month = input("Enter the month: ")
        if month == "February":
            day = int(input("Enter your birthday: "))
            if day < 31 and day > 30:
                print("Error")
            else:
                print("You entered wrong")
        print("Error")
    elif age < 0:
        print("Cannot enter negative number")
    else:
    	print(f"Error\n{the_end}")

except ValueError:
    print("Error\n{}".format(the_end))


except KeyboardInterrupt:
	print("\nDastur tugadi")
