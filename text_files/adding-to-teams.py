file = open("teams.txt", "r")

outfile = "This is a new line\n"

for line in file.readlines():
    outfile += line

file = open("teams.txt", "w")
file.write(outfile)
file.close()
