math_mark = int(input("Please enter your math mark \n"))
chem_mark = int(input("Please enter your chemestry mark\n"))
phy_mark = int(input("Please enter your physics mark\n"))

total_mark = (math_mark + chem_mark + phy_mark)/3

if(total_mark < 40):
    print("you failed")
elif(total_mark >=40 and total_mark<50):
    print("D")
elif(total_mark >=50 and total_mark<60):
    print("C")
elif(total_mark >=60 and total_mark<70):
    print("B")
else:
    print("A")

