

def draw_line(num = 10, add_blanka = True):
    for rad in range(num):
        if add_blanka == True:
            for blanka in range(rad):
                print( " ", end=" ")
        for i in range(num - rad):
            print(i, end=" ")
        print()
draw_line(10)
draw_line(10, False)

  

    