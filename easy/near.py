firstWord = input("please enter the first word\n")
secondWord = input("please enter the second word\n")

print("near(" + firstWord + "), (" + secondWord + ")")

firstwordList = isbnList = [char for char in firstWord]
secondwordList = isbnList = [char for char in firstWord]

count = -1
removed = False
Possible = False

for x in firstwordList:
    count =+ 1
    while len(secondwordList) >= count:
        if (firstwordList[count] != secondwordList[count]) and removed == False:
            del firstwordList[count]
            print("first statement at " + str(count))
            Possible = True
        if firstwordList[count] != secondwordList[count]:
            notPossible = False
            print("second statement at " + str(count))
            break

print(Possible)
