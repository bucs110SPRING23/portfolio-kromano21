def star_pyramid():
    rows = int(input("How many rows?"))
    for r in range(rows):
        row = "*" * (r + 1)
        print(row)

def rstar_pyramid():
    rows = int(input("How many rows?"))
    for r in range(rows):
        row = "*" * (rows - r)
        print(row)