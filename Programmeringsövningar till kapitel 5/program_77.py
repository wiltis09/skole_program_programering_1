print(int("9 18 27 36 45 54 63 72 81 ".__sizeof__()) - 41)



def draw_line(plus = False, num = 10, plus_num = 0):
    line = ""
    for i in range(1, num):
        if plus:
            line = (str(line) + str(i * plus_num) + " ")
        else:   
            line = (str(line) + str(i) + " ")
    if not (line.__sizeof__() - 41) == 26:
        print(line.__sizeof__() - 41)
        for i in range(1, (26 - (line.__sizeof__() - 41))):
            line = line + " "
    print(line)
draw_line(False, 10, 0)
draw_line(True, 10, 2)
draw_line(True, 10, 4)
draw_line(True, 10, 5)
draw_line(True, 10, 6)
draw_line(True, 10, 7)
draw_line(True, 10, 8)
draw_line(True, 10, 9)
  