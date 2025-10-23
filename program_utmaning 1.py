
import random
import textwrap



def input_number(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value 
        except:
            print("Please enter a valid integer.")
            
dagar = [
    "mondag",       # BMI < 18.5
    "tristag",      # BMI 18.5 – 24.9
    "onsaga",        # BMI 25 – 29.9
    "torstag",     
    "fredag",
    "lördag",
    "söndag",
]



print(" ")
print(" ")
print("==== BMI CALCULATOR ====")
print(" ")

acktiviterer_mondag = []
acktiviterer_tristag = []
acktiviterer_onsaga = []
acktiviterer_torstag = []
acktiviterer_fredag = []
acktiviterer_lördag = []
acktiviterer_söndag = []

def ask_for_day_events():
    for i in dagar:
        prompt = str("hur många acriviteter har du på " + i + ":")
        aktivtet_mänged= input_number(prompt)
        for j in range(aktivtet_mänged):
            aktivitet = input("Skriv in aktiviteten: ")
            if i == "mondag":
                acktiviterer_mondag.append(aktivitet)
            elif i == "tristag":
                acktiviterer_tristag.append(aktivitet)
            elif i == "onsaga":
                acktiviterer_onsaga.append(aktivitet)
            elif i == "torstag":
                acktiviterer_torstag.append(aktivitet)
            elif i == "fredag":
                acktiviterer_fredag.append(aktivitet)
            elif i == "lördag":
                acktiviterer_lördag.append(aktivitet)
            elif i == "söndag":
                acktiviterer_söndag.append(aktivitet)
print(str(acktiviterer_mondag))
ask_for_day_events()


