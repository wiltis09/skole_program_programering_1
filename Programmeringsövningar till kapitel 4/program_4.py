
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
bensinpris = input_number("hur är priset för bensin nu?: ")

if bensinpris <= 10:
    bensinpris_text = bensinpris_beskrivning[0]
elif bensinpris > 10 and bensinpris <= 15:
    bensinpris_text = bensinpris_beskrivning[1]
elif bensinpris > 15 and bensinpris <= 20:
    bensinpris_text = bensinpris_beskrivning[2] 
elif bensinpris > 20:
    bensinpris_text = bensinpris_beskrivning[3]
print(bensinpris_text)