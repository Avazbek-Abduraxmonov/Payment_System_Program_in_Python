# try:
# 	the_end = "Dastur tugadi"
# 	age = int(input("Yoshingizni kiriting: "))

# 	if age>=18:
# 		month = input("Oyni kiriting: ")
# 		if month =="fevral":
# 			day = int(input("Tug'ilgan kuningizni kiriting: "))
# 			if day < 31 or day < 30:
# 				print("xato")
# 			else:
# 				print("Notog'ri kiritdingiz")
# 	if age<=87:
# 		print(f"Yoshingiz 87dan oshib ketgan ekan")
# 		print(the_end)	
# 	elif age <0:
# 		print("Manfiy son kiritish mumkin emas")		
# except ValueError:
# 	print("Xatolik\n{}".format(the_end))


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