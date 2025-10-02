print("Input two numbers:")


bodidii = int(print(input("1")))

def input_number(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except:
            print("Please enter a valid integer.")

input_num_1 = input_number("First number: ")
input_num_2 = input_number("Second number: ")

num_summe = input_num_1 + input_num_2
num_produckt = input_num_1 * input_num_2
print(input_num_1, "+", input_num_2, "är lika med", num_summe, "summan")
print(input_num_1, "*", input_num_2, "är lika med", num_produckt, "produkten")
print("Tack för att du använde programmet!")