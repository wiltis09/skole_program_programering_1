
def input_number(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except:
            print("Please enter a valid integer.")

while True:
    ålder = input_number("Hur gammal är du:")
    if ålder < 18:
        print("tyvärr kan vi inte bevilja fakturabetalning")
        break
    else:
        årsinkomsten = input_number("Hur mycket är din årliga inkomst:")
        if årsinkomsten < 120000:
            print("tyvärr kan vi inte bevilja fakturabetalning")
            break
        else:
            kreditanmärkningar = input_number("Hur många kreditanmärkningar har du?:")
            if kreditanmärkningar > 0:
                print("tyvärr kan vi inte bevilja fakturabetalningen")
                break
            else:
                print("Fakturabetalning beviljad")

print("Tack för att du använde programmet!")