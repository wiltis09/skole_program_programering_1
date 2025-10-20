import math
import sys 

print("Input three float numbers below")

def input_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 1000:
                return value
        except:
            print("Please enter a valid float.")

input_num_1 = input_number("First number: ")
input_num_2 = input_number("Second number: ")
input_num_3 = input_number("Third number: ")


variabel_summa = input_num_1 + input_num_2 + input_num_3
ivariabel_summa_dicimal = (f"{variabel_summa:.2f}")
print("Tack för att du använde programmet!")
print("")
print("")
print("")
def print_num1(num1, num2, num3):
    width = 4 #len(str(num))
    inputs = [(f"{num1:.2f}"),(f"{num2:.2f}"),(f"{num3:.2f}")]
    s1 = str(num1 + num2 + num3)
    for num in inputs:
        if len(str(num)) > 3:
            width = width + (len(str(num)) - 2)
    for num in inputs:
        s = str(num)
        if num == inputs[2]:
            print( "+  " + s.rjust(width - 1))
        else:
            if len(str(num)) > 3:
                print( "  " + s.rjust(width))
            else:
                print("  " + s.rjust(width))
    spacer = "" 
    for l in range(0, width):
        spacer = str(spacer) + "="
    print(spacer + "===")
    print("  " + s1.rjust(width))
print_num1(input_num_1, input_num_2, input_num_3)
print("")
print("")
print("")