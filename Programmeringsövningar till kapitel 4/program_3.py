
import random

def input_number(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value 
        except:
            print("Please enter a valid integer.")

a = int(print(input_number("vad är a:")))
c = int(print(input_number("vad är c:")))
b = int(print(input_number("vad är b:")))
if (a < b and not b < c) or (b < c and not a < b):
    
    print("antigen är a mindre än b eller b mindre än c")

