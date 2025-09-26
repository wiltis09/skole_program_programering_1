
import random
import textwrap

BMI_klasser = [
    "Underviktig",       # BMI < 18.5
    "Normalviktig",      # BMI 18.5 – 24.9
    "Överviktig",        # BMI 25 – 29.9
    "Fetma klass 1",     # BMI 30 – 34.9
    "Fetma klass 2",     # BMI 35 – 39.9
    "Fetma klass 3"      # BMI ≥ 40
]


# Om man vill kan man även lägga till typiska beskrivningar
BMI_klasser_beskrivning = [
    "Alltför låg vikt – risk för näringsbrist\n och hälsoproblem",
    "Normal vikt – låg risk för viktrelaterade\n hälsoproblem",
    "Lite över normalvikt – ökad risk för\n hälsoproblem",
    "Fetma klass 1 – betydande risk för\n hjärt-kärlsjukdomar",
    "Fetma klass 2 – hög risk för\n allvarliga hälsoproblem",
    "Fetma klass 3 – mycket hög risk för\n allvarliga sjukdomar"
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
    BMI_klass = BMI_klasser[0]
    BMI_klass_text = BMI_klasser_beskrivning[0]
elif BMI > 18.5 and BMI < 24.9:
    BMI_klass = BMI_klasser[1]
    BMI_klass_text = BMI_klasser_beskrivning[1]
elif BMI > 25 and BMI < 29.9:
    BMI_klass = BMI_klasser[2]
    BMI_klass_text = BMI_klasser_beskrivning[2] 
elif BMI > 30 and BMI < 34.9:
    BMI_klass = BMI_klasser[3]
    BMI_klass_text = BMI_klasser_beskrivning[3]
elif BMI > 35 and BMI < 39.9:
    BMI_klass = BMI_klasser[4]
    BMI_klass_text = BMI_klasser_beskrivning[4]
elif BMI > 40:
    BMI_klass = BMI_klasser[5]
    BMI_klass_text = BMI_klasser_beskrivning[5]

print("Ditt BMI är:", f"{BMI:.1f}")

box_width = 27
print("┌" + "─" * (box_width - 2) + "┐")
print("│{:^{width}}│".format("~ BMI REPORT ~", width=box_width-2))
print("├" + "─" * (box_width - 2) + "┤")
print("│{:^{width}}│".format(f"BMI Klass: {BMI_klass}", width=box_width-2))
print("│{:^{width}}│".format("Beskrivning:", width=box_width-2))

# Dela upp beskrivningen i rader som får plats
for line in textwrap.wrap(BMI_klass_text, box_width-2):
    print("│{:^{width}}│".format(line, width=box_width-2))

print("└" + "─" * (box_width - 2) + "┘")