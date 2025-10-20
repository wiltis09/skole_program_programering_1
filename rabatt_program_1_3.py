
import random




varo_lista = ["penna", "sudd", "linjal", "ritblock", "bok", "dator", "mobiltelefon", "hörlurar", "mus", "tangentbord", "skrivare", "bord", "stol", "lampa", "väggklocka", "fönster", "dörr", "garderob", "hylla", "spegel", "matta", "blomma", "vas", "tavla", "klocka", "kamera", "mikrofon", "högtalare", "projektor", "TV", "kylskåp", "frys", "spis", "ugn", "diskmaskin", "tvättmaskin", "torktumlare", "dammsugare", "stryktärn", "stryktbräda", "sopborste", "skurhink", "mopp", "hink", "stege", "verktygslåda", "skruvmejsel", "hammare", "såg", "skiftnyckel", "tång", "skruvar", "spikar", "muttrar", "bultar", "måttband", "vattenpass", "fogsvans", "pensel", "roller", "färg", "lim", "tejp", "sandpapper", "spackel", "skrapa", "skyddsglasögon", "hörselskydd", "handskar", "hjälm", "arbetskläder", "säkerhetssele", "brandsläckare", "första hjälpen-kit"]
vara = random.choice(varo_lista)
print("Hi how moutch dos a", vara, "cost?")
def input_number(prompt1, prompt2, prompt3):
    prompt = str(prompt1)+" "+str(prompt2)+" "+str(prompt3)
    while True:
        try:
            value = int(input(prompt))
            return value
        except:
            print("Please enter a valid integer.")
import random


input_num_1 = input_number("The pris of a:", vara, "is: ")
print("The", vara, "costs:", input_num_1, "kr")

num_med_rabatt = int(input_num_1 * 0.15)
print("You got a discont off 15%. Now your", vara, "only cost:", num_med_rabatt, "kr")
print("thank you for using the program!")