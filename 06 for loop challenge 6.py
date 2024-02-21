total = int(0)

for i in range(5):
    numb = int(input("Enter a number "))
    add = input("Do you want to add this number? ")
    if add == "y":
        total += numb

print(total)
