p = int (input("Ange poäng på provet: "))

if p >= 90:
    print ("betyg = A")
else:
    if p >= 80:
        print ("betyg = B")
    else:
        if p >= 70:
            print ("betyg = C")
        else:
            if p >= 60:
                print ("betyg = D")
            else:
                if p >= 50:
                    print ("betyg = E")
                else:
                    print ("betyg = F")