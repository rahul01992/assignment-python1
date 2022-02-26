print("Answere number 2")
from math import factorial
n=int(input('Enter the size of pascals triangle '))

print("By use of function")

for i in range(n):
	for j in range(n-i+1):
		print(end=" ")

	for j in range(i+1):
		print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")	#(Binomial Formula) nCr = n!/((n-r)!*r!)
	print()
print("\n\n")

print("By Use of Recursion")

def pascal_triangle(n,originalength=n):
    if n == 0:
        return
    pascal_triangle(n-1,originalength)
    #print spaces
    print('  '*(originalength-n), end='')

    #start with 1
    start = 1
    for i in range(1, n+1):

        print(start, end ='   ')

        #using Binomial Coefficient
        start = start * (n - i) // i
    print()
pascal_triangle(n)
print("\n")


