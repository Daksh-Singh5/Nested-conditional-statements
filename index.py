medical = input("Did you have any medical: ")
attendence =int(input("Type the percent of your attendence: "))
if medical == "y":
    print("You are allowed to take the exam")
else:
    if attendence > 75:
        print("you are allowed to take the exam")
    else:
        print("you are not allowed to take the exam")
