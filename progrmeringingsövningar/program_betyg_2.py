while True:
    try:
        p = int(input("Ange poäng på provet: "))
        if p >= 90:
            print ("betyg = A")
            break
        else:
            if p >= 80:
                print ("betyg = B")
                break
            else:
                if p >= 70:
                    print ("betyg = C")
                    break
                else:
                    if p >= 60:
                        print ("betyg = D")
                        break
                    else:
                        if p >= 50:
                            print ("betyg = E")
                            break
                        else:
                            print ("betyg = F")
                            break
    except:
        print("Please enter a valid integer. 66")
        