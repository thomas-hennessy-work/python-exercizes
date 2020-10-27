file = open("teams.txt", "r")

outfile = ""

for line in file:
    if line == 1 or 4:
        print(file.readline())
    else:
        file.readline()

file.close()