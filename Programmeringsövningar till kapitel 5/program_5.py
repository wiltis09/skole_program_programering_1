
import random

def input_number(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value 
        except:
            print("Please enter a valid integer.")


bensinpris_beskrivning = [
    "Det var billigt!",
    "Tanka fukk tank",
    "Tanka tio liter",
    "Nu säljer jag bilen och cyklar i stället",
]
bensinpris_text = str
år = input_number("ge mig ett år tal: ")

def test_calc(år):
    print("error0")
    if (float(år) / 4) == int((float(år) / 4)):
        print("error1")
        if år > 1753:
            if år != 1800 and år != 1900:
                print("error2")
                return"år tallet är ett skot år"
            else:
                return"dit år tal är intet ett skot år "
        else:
            print("error3")
            return"år tallet moster var mer en 1753"
    else:
        return"dit år tal är intet ett skot år "

print(test_calc(år))