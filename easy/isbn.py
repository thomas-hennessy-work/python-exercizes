isbn = input("Please input the first 12 digits of the ISBN \n")
isbnList = []
isbnListClean =[]
total = int(0)

count = int(-1)

# https://www.geeksforgeeks.org/python-split-string-into-list-of-characters/
isbnList = [char for char in isbn]

# for x in isbnList:
#     if x != "-":
#         if int(x)%2 == 0:
#             print(str(x) + " is even")
#             print("add " + str(x))
#             total = total + int(x)
#             print("total is " + str(total))
#         else:
#             print(str(x) + " is odd")
#             print("add " + str(int(x)*3))
#             total = total + (int(x)*3)
#             print("total is " + str(total))

for x in isbnList:
     if x != "-":
         isbnListClean.append(x)

for y in isbnListClean:
    count += 1
    if (int(count%2) == 0):
        total += int(y)
        print(total)
    else:
        total += int(int(y)*3)
        print(total)

total = (10 - (total%10))
print("The last digit will be " + str(total))