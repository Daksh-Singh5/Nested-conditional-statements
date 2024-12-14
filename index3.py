vehicle = input("Which vehicle do you want \n1.Bike \n2.Car\nEnter your choice ")
if vehicle == "1":
    brand = input("Which brand \n1.BMW \n2.Honda")
    if brand == "1":
        print("Your ride is fixed with a bike of the brand BMW")
    elif brand == "2":
        print("Your ride is fixed with a bike of the brand Honda")
    else:
        print("Wrong number entered")
elif vehicle == "2":
    brand = input("Which brand \n1.BMW \n2.Honda")
    if brand == "1":
        print("Your ride is fixed with a car of the brand BMW")
    elif brand == "2":
        print("Your ride is fixed with a car of the brand Honda")
    else:
        print("Wrong number entered")
else:
    print("Wrong number entered")