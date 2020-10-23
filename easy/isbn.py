isbn = input("Please input the first 12 digits of the ISBN \n")
isbnList = []
total = float(0)

# https://www.geeksforgeeks.org/python-split-string-into-list-of-characters/
isbnList = [char for char in isbn]

for x in isbnList:
    if x != "-":
        if float(x)%2 == 0:
            total = total + float(x)
        else:
            total = total + (float(x)*3)

print(int(10 - (total%10)))