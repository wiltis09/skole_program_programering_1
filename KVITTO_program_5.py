
import random

kassör_name_lista = ["Raad", "Wilton", "Mario", "Zelda", "link", "bob", "Astrid", "Harry Poter", "Nicolina"]
pump_name_lista = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
bensin_typ_name_lista = ["Bensin", "El", "Disel"]
bensin_typ_Pris_name_lista = ["Pris/liter", "Pris/kWh"]
# Lista över bensinbilar
bensinbil_typ_name_lista = [
    "Ferrari 488",
    "Ferrari F8",
    "Ferrari Roma",
    "Lamborghini Huracán",
    "Lamborghini Aventador"
]

# Lista över elbilar
elbil_typ_name_lista = [
    "Tesla: Model 3",
    "Tesla: Model Y",
    "Tesla: Model S",
    "Tesla: Model X",
    "Volkswagen: ID",
    "Polestar 2",
    "Polestar 3"
]

# Lista över dieselbilar
dieselbil_typ_name_lista = [
    "Volkswagen Golf",
    "Volkswagen Passat",
    "Volkswagen Tiguan",
    "Audi A3",
    "Audi Q5",
    "BMW X3",
    "BMW X5",
    "Mercedes-Benz C-klass",
    "Mercedes-Benz E-klass",
    "Volvo V60",
    "Volvo V90",
    "Ford Focus",
    "Skoda Octavia",
    "Skoda Superb",
    "Nissan Qashqai"
]


payment_methods_name_lista = ["Visa", "MasterCard", "American Express", "Apple Pay", "Google Pay", "Swish", "Cash", "Klarna", "Samsung Pay", "PayPal", "Gift cards", "Cryptocurrency"]


payment_methods_name = "(" + random.choice(payment_methods_name_lista) + ")"
PUMP_name = random.choice(pump_name_lista)
Kassör_name = random.choice(kassör_name_lista)
Bensin_typ_name = random.choice(bensin_typ_name_lista)
Card_nummber = random.randrange(1000, 9999)
Ref_nummber = random.randrange(10000000, 99999999)
car_typ_name = ""
bensin_typ_Pris_name = ""
if Bensin_typ_name == "Bensin":
    car_typ_name = random.choice(bensinbil_typ_name_lista)
    bensin_typ_Pris_name = bensin_typ_Pris_name_lista[0]
elif Bensin_typ_name == "El":
    car_typ_name = random.choice(elbil_typ_name_lista)
    bensin_typ_Pris_name = bensin_typ_Pris_name_lista[1]
elif Bensin_typ_name == "Disel":
    car_typ_name = random.choice(dieselbil_typ_name_lista)
    bensin_typ_Pris_name = bensin_typ_Pris_name_lista[0]
PUMP_name_med_nolla = "0" + PUMP_name
PUMP_name_med_med_titel = "PUMP-" + PUMP_name

print(payment_methods_name)
def input_number(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except:
            print("Please enter a valid integer.")

input_Volym = input_number("hur mycket har du tankad din " + car_typ_name + " (i liter): ")
input_Pris_per_liter = input_number("vad är Pris/liter för " + Bensin_typ_name + " i kronor: ")






print("                           ✦✦ KVITTO ✦✦") 
print("                          Macken \"Full Tank\"") 
print("                Vi fyller dig – inte bara bilen!") 
print("------------------------------------------------------------------------------") 
print("Datum: 26-09-2025   Tid: 21:37") 
print("Pump: ", PUMP_name_med_nolla, "     Terminal: ", PUMP_name_med_med_titel, "      Kassör: ", Kassör_name) 
print("------------------------------------------------------------------------------") 
print("Artikel: ", Bensin_typ_name) 
print("  Volym: ", input_Volym,"L") 
print(bensin_typ_Pris_name, input_Pris_per_liter, "kr") 
print("  Bil: ", car_typ_name) 
print("  Belopp ...... ", (input_Volym * input_Pris_per_liter), "kr") 
print("------------------------------------------------------------------------------") 
print("TOTAL att betala ........... ",(input_Volym * input_Pris_per_liter), "kr")
print("Betalsätt: ", payment_methods_name) 
print("Kortnr: **** **** **** ", Card_nummber, "   Godkänt: JA") 
print("Ref.nr: ", Ref_nummber) 
print("------------------------------------------------------------------------------") 
print("🚗 Tack för att du tankade hos Vroom Vroom Station!") 
print("    Kör försiktigt — och kom gärna förbi på") 
print("        Ref.nr: ", Ref_nummber) 
print("Tack för att du använde programmet!")
