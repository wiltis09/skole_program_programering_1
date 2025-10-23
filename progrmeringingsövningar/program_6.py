
import math
import sys 


print("Input thire numbers:")

def input_number(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except:
            print("Please enter a valid integer.")

input_num_1 = 1 #input_number("First number: ") 
input_num_2 = 1 #input_number("Second number: ")
input_num_3 = input_number("Third number: ")


print ((len(str(input_num_1)) - (len(str(input_num_1)) - 1)))
def print_num1(num1, num2, num3):
    width = 4 #len(str(num))
    inputs = [num1,num2,num3]
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
variabel_summa = input_num_1 + input_num_2 + input_num_3
print("Tack för att du använde programmet!")
print("")
print("")
print("")


print(print_num1(input_num_1, input_num_2, input_num_3))