




print("°C".ljust(20), "°F".ljust(20))
for k in range(1, 30):
    print("-", end="")
print("")
for i in range(-40, 40):
    print("|", (str(i) + "°C").ljust(10), "|".ljust(5), (str(round(32 + i * 9/5)) + "°F").ljust(10), "|")
for k in range(1, 55):
    print("-", end="")
print("")