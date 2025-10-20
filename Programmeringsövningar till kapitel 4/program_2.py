
import random

BMI_klasser_beskrivning = [
    "Du har undervikt",
    "Du har normalvikt",
    "Du har övervikt",
    "Du har tyvärr fetma",
]



print(" ")
print(" ")
print("==== BMI CALCULATOR ====")
print(" ")
def input_number(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value 
        except:
            print("Please enter a valid integer.")

input_vikt = input_number("hur mycket väger du: ")
input_längd = input_number("vad är din längd i cm: ") 


BMI = input_vikt / ((input_längd / 100) ** 2)

BMI_klass = ""
BMI_klass_text = ""
if BMI < 18.5:
    BMI_klass_text = BMI_klasser_beskrivning[0]
elif BMI > 18.5 and BMI < 24.9:
    BMI_klass_text = BMI_klasser_beskrivning[1]
elif BMI > 25 and BMI < 29.9:
    BMI_klass_text = BMI_klasser_beskrivning[2] 
elif BMI > 30 and BMI < 34.9:
    BMI_klass_text = BMI_klasser_beskrivning[3]



print("Ditt BMI är:", f"{BMI:.1f}")
print(BMI_klass_text)
