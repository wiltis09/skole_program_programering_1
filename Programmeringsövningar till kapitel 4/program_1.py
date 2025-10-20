print("poäng på tre prov:")

def input_number(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except:
            print("Please enter a valid integer.")
def medelvärde_calc(prov_1, prov_2, prov_3):
    total = int((prov_1 + prov_2 + prov_3) // 3)
    if total > 90:
        return "medelvärde är " + str(total) +  "    Bra jobbat!"
    else:
        return "medelvärde är " + str(total)

prov_poäng_1 = input_number("vad fick du för poäng på prov 1:")
prov_poäng_2 = input_number("vad fick du för poäng på prov 2:")
prov_poäng_3 = input_number("vad fick du för poäng på prov 3:")

print(medelvärde_calc(prov_poäng_1,prov_poäng_2, prov_poäng_3))
print("Tack för att du använde programmet!")