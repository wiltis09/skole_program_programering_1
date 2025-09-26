
import random




varo_lista = ["penna", "sudd", "linjal", "ritblock", "bok", "dator", "mobiltelefon", "hörlurar", "mus", "tangentbord", "skrivare", "bord", "stol", "lampa", "väggklocka", "fönster", "dörr", "garderob", "hylla", "spegel", "matta", "blomma", "vas", "tavla", "klocka", "kamera", "mikrofon", "högtalare", "projektor", "TV", "kylskåp", "frys", "spis", "ugn", "diskmaskin", "tvättmaskin", "torktumlare", "dammsugare", "stryktärn", "stryktbräda", "sopborste", "skurhink", "mopp", "hink", "stege", "verktygslåda", "skruvmejsel", "hammare", "såg", "skiftnyckel", "tång", "skruvar", "spikar", "muttrar", "bultar", "måttband", "vattenpass", "fogsvans", "pensel", "roller", "färg", "lim", "tejp", "sandpapper", "spackel", "skrapa", "skyddsglasögon", "hörselskydd", "handskar", "hjälm", "arbetskläder", "säkerhetssele", "brandsläckare", "första hjälpen-kit"]
vara = random.choice(varo_lista)
print("hej vad koser en:", vara)
def input_number(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except:
            print("Please enter a valid integer.")
import random


input_num_1 = input_number("kosnad: ")
print("en", vara, "kostar:", input_num_1, "kr")

input_rabbat = input_number("hur mycket rabatt vill du ha? ")

rabatt_procent = input_rabbat / 100
print(rabatt_procent)
num_med_rabatt = int(input_num_1 * rabatt_procent)
print("du får rabatt på din", vara, "du fick", input_rabbat,"%"  "rabbat så nu kostar din", vara, "bara:", num_med_rabatt, "kr")
print("Tack för att du använde programmet!")