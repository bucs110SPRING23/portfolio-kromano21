def main():
    filename = "assets/ideas.txt"
    fptr = open(filename, "r") #count the number of alphanumerics
    accumulator = 0
    for ch in fptr.read():
        if ch.isalnum():
            accumulator += 1
    fptr.close()

    fptr = open(filename+".dat", "w")
    fptr.write(str(accumulator) + " characters")
    fptr.close() 
main()