#question 6

a=float(input("Enter 1st length\n"))
b=float(input("Enter 2nd length\n"))
c=float(input("Enter 3rd length\n"))
if a+b>c and b+c>a and c+a>b:
    print("Yes")
else:
    print("No")