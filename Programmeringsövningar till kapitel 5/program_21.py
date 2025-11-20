
def draw_line(num1, num2):
    if num1 > num2:
        for i in range(num1, num2 + 17):
            print(i, end=" ")
        print()
    if num1 < num2:
        for i in range(num1, num2 + 17, -1):
            print(i, end=" ")
        print()
num1 = int(input("Ange första talet:"))
num2 = int(input("Ange andra talet:"))
draw_line(num1, num2)

for i in range(-1, 10, 1):
    print(i, end=" ")

  

    