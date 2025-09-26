

def input_triangle(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except:
            print("Please enter a valid integer.")

input_trianglens_bas = input_triangle("förste skriv in triangelns bas: ")
input_trianglens_höjd = input_triangle("förste skriv in triangelns höjd: ")

trianglens_area = (input_trianglens_bas * input_trianglens_höjd) / 2
print(input_trianglens_bas, "*", input_trianglens_höjd, "/ 2", "är lika med", trianglens_area, "vilket är lika med trianglens_area")
print("triangelns area är lika med", trianglens_area)
print("Tack för att du använde programmet!")