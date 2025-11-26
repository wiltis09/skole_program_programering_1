




print("num".ljust(20), "Kvadrater".ljust(20), "Kuber")
for k in range(1, 55):
    print("-", end="")
print("")
for i in range(1, 20):
    
    print("|", str(i).ljust(2), "|".ljust(15), "|", str(i * i).ljust(3), "|".ljust(15), "|", str(i * i * i).ljust(4), "|", )
for k in range(1, 55):
    print("-", end="")
print("")