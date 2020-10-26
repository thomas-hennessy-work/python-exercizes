firstWord = input("please enter the first word\n")
secondWord = input("please enter the second word\n")

print("near(" + firstWord + "), (" + secondWord + ")\n\n")

firstwordList = isbnList = [char for char in firstWord]
secondwordList = isbnList = [char for char in secondWord]

count = -1
removed = False
Possible = False

for letter in firstwordList:
    count += 1
    if count < len(secondwordList):
        if (letter != secondwordList[count]) and removed == False:
            Possible = True
            removed = True
        elif letter != secondwordList[count]:
            Possible = False
            break

print(Possible)
