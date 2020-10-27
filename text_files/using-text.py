# opens the text file in read
file = open("random_text.txt", "r")

# stores the data we want to keep
outfile = ""

# stores every second line in a var
for line in range(1, 10):
    if line % 2 == 0:
        outfile += file.readline()
    else:
        file.readline()

# deletes everything and writes ther strored text in to the file
file = open("random_text.txt", "w")
file.write(outfile)
file.close