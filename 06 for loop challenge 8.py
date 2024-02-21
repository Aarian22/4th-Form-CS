people = int(input("How many people do you want to invite? "))

if people < 10:
    for i in range(people):
        name = input("Enter the name of the person to invite ")
        print(name, "has been invited!")
else:
    print("Too many people!")
