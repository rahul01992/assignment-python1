#question 4

a=int(input("Enter 1st number\n"))
b=int(input("Enter 2nd number\n"))
c=int(input("Enter 3rd number\n"))
print(a)
print(b)
print(c)
if a>b and a>c:
    print(a," is greater then among three number")
elif b>c and b>a:
    print(b," is greater then among three number")
elif c>a and c>b:
    print(c," is greater then among three number")