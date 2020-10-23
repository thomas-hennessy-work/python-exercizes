math_mark = int(input("Please enter your math mark \n"))
chem_mark = int(input("Please enter your chemestry mark\n"))
phy_mark = int(input("Please enter your physics mark\n"))

total_mark = (math_mark + chem_mark + phy_mark)/3

print("Your percentage score is: " + str(total_mark) + "%")

if(total_mark < 40):
    print("you failed")
elif(total_mark >=40 and total_mark<50):
    print("You scored a grade of: D")
elif(total_mark >=50 and total_mark<60):
    print("You scored a grade of: C")
elif(total_mark >=60 and total_mark<70):
    print("You scored a grade of: B")
else:
    print("You scored a grade of: A")

