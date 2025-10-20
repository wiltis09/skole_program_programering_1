
datum = int(2025)

def print_spacer(length):
    specer = ""
    for i in range(0, length):
        print(specer)
def print_input_prompt(prompt, check_type = False, Type = int):
    if not check_type:
        value = pritn(input(prompt))
        return value
    while True:
        try:
            value = print(Type(input(prompt)))
            return value
        except:
            print("Please enter a valid", check_type)
def print_two_part_prints(part1, part2,):
    while True:
        try:
            print(str(part1) + (" ") + str(part2))
            return
        except:
            print("error")
def print_three_part_prints(part1, part2, part3):
    print(str(part1) + str(part2) + str(part3))
print_spacer(50)
name = print_input_prompt("Mata in dit namn:", False, int)
print_two_part_prints("dit namn är", name, str)
hetal2 = int(input("mata in ett heltal:") )
print_spacer(1)

ålder = input("Mata in din ålder:") 
födelseår = datum - int(ålder)

print_two_part_prints("din ålder är", ålder)
print_two_part_prints("du föddes år", födelseår)

print_spacer(1)

flyttal1 = float(input("Mata in ett flyttal:") )

print_two_part_prints("Du matade in", flyttal1)
print_three_part_prints(flyttal1, " genom 2 är ", flyttal1 / 2)

print_spacer(1)

hetal1 = int(input("mata in ett heltal:") )

print(str("Du matade in ") + ("|") + str(hetal1) + ("|"))

print_spacer(1)

flyttal2 = float(input("Mata in ett flyttal:") )

print_two_part_prints("Du matade in", (f"{flyttal2:.4f}"))

print(str(""))

hetal2 = int(input("mata in ett heltal:") )
flyttal3 = float(input("Mata in ett flyttal:") )
print_two_part_prints("Du matade in ", hetal2)
print_two_part_prints("Och", (f"{flyttal3:.4f}"))


