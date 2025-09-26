print("Input two numbers:")

def input_number(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except:
            print("Please enter a valid integer.")

input_num_1 = input_number("First number: ")
input_num_2 = input_number("andra number: ")
input_num_3 = input_number("tredj number: ")

variabel_summa = input_num_1 + input_num_2 + input_num_3
print("Tack för att du använde programmet!")
print("")
print("")
print("")
if input_num_1 < 10:
    print("    ", input_num_1)
elif input_num_1 < 100:
    print("   ", input_num_1)
elif input_num_1 < 1000:
    print("  ", input_num_1)

if input_num_2 < 10:
    print("    ", input_num_2)
elif input_num_2 < 100:
    print("   ", input_num_2)
elif input_num_2 < 1000:
    print("  ", input_num_2)

if input_num_3 < 10:
    print("+   ", input_num_3)
elif input_num_3 < 100:
    print("+  ", input_num_3)
elif input_num_3 < 1000:
    print("+ ", input_num_3)

print("======")
if variabel_summa < 10:
    print("    ", variabel_summa)
elif variabel_summa < 100:
    print("   ", variabel_summa)
elif variabel_summa < 1000:
    print("  ", variabel_summa)
print("")
print("")
print("")