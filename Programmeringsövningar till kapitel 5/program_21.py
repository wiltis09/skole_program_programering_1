num1 = input("Ange första talet: ")
num2 = input("Ange Andra talet: ")
if num1 < num2:
    for i in range (int(num1), int(num2) +1 ):
        print(i, end="d")
    print("")
elif num1 > num2:
    for i in range(int(num1), int(num2), -1):
        print(i, end="w")
    print("")