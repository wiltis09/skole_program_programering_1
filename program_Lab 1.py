name = input("Mata in dit namn:") 

print(str("dit namn är") + (" ") + str(name))

ålder = input("Mata in din ålder:") 

print(str("din ålder är") + (" ") + str(ålder))

datum = int(2025)
födelseår = datum - int(ålder)
print(str("du föddes år") + (" ") + str(födelseår))

flyttal1 = float(input("Mata in ett flyttal:") )

print(str("Du matade in") + (" ") + str(flyttal1))
print( str(flyttal1) + str(" genom 2 är ") + str(flyttal1 / 2))

hetal = int(input("mata in ett heltal:") )

print(str("Du matade in ") + ("|") + str(hetal) + ("|"))

flyttal2 = float(input("Mata in ett flyttal:") )

print(str("Du matade in") + (" ") + str((f"{flyttal2:.9900f}")))

