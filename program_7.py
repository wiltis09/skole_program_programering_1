print("Input three numbers below 1000:")

def input_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 1000:
                return value
        except:
            print("Please enter a valid float.")

input_num_1 = input_number("First number: ")
input_num_2 = input_number("andra number: ")
input_num_3 = input_number("tredj number: ")

input_num_1_dicimal = (f"{input_num_1:.2f}")

input_num_2_dicimal = (f"{input_num_2:.2f}")

input_num_3_dicimal = (f"{input_num_3:.2f}")

variabel_summa = input_num_1 + input_num_2 + input_num_3
ivariabel_summa_dicimal = (f"{variabel_summa:.2f}")
print("Tack för att du använde programmet!")
print("")
print("")
print("")
if input_num_1 < 10:
    print("    ", input_num_1_dicimal)
elif input_num_1 < 100:
    print("   ", input_num_1_dicimal)
elif input_num_1 < 1000:
    print("  ", input_num_1_dicimal)

if input_num_2 < 10:
    print("    ", input_num_2_dicimal)
elif input_num_2 < 100:
    print("   ", input_num_2_dicimal)
elif input_num_2 < 1000:
    print("  ", input_num_2_dicimal)

if input_num_3 < 10:
    print("+   ", input_num_3_dicimal)
elif input_num_3 < 100:
    print("+  ", input_num_3_dicimal)
elif input_num_3 < 1000:
    print("+ ", input_num_3_dicimal)

print("======")
if variabel_summa < 10:
    print("    ", ivariabel_summa_dicimal)
elif variabel_summa < 100:
    print("   ", ivariabel_summa_dicimal)
elif variabel_summa < 1000:
    print("  ", ivariabel_summa_dicimal)
print("")
print("")
print("")