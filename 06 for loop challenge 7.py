direction = input("Up or down ")

if direction == "u":
    numb = int(input("Enter a number "))
    for i in range(numb):
        print(i+1)
elif direction == "d":
    numb = int(input("Enter a number less than 20 "))
    for i in range(numb):
        if (20 - i) >= numb:
            print(20 - i)
else:
    print("I dont understand")
