print("")
name = input("Ange ditt namn:")
lgd = len(name)
i = lgd - 1
print("Baklänges blir det : ", end="")
while i >= 0:
    print(name[i], end="")
    i = i - 1
print("")
print("")

