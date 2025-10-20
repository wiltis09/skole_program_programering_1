print("poäng på tre prov:")

def input_number(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except:
            print("Please enter a valid integer.")

ålder = input_number("Hur gamal är du:")
årsinkomsten = input_number("Hur mycket är din årliga inkomest:")
kreditanmärkningar = input_number("Hur många kreditanmärkningar har du?:")

if ålder > 18 and årsinkomsten >= 120000 and kreditanmärkningar == 0:
    print("Fakturabetalning beviljad")
else:
     print("Tyvär kan vi inte bevilja fakturabetalning beviljad")
print("Tack för att du använde programmet!")