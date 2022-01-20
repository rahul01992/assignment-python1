# assignment-python1
xxyy
#    ASSIGNMENT 1
#QUES 1 

num1=int(input("enter the value of num1:"))
num2=int(input("enter the value of num2:"))
num3=int(input("enter the value of num3:"))
average= float((num1+num2+num3)/3)
print("the Average of three numbers you entered is :",average)


#QUES 2
# take input from user of their gross income 
# and no. of dependents
gross_income = int(input("Enter your Gross income: "))

Dependents = int(input("enter the number of dependents: "))
standard_deduction = 10000 #all taxpayers are allowed this standard deduction
deduction =3000 #it is the deduction per dependents
Tax_rate =0.20 # the tax rate 20%
Taxable_income = gross_income-standard_deduction-(Dependents*deduction)
Tax = float(Taxable_income*Tax_rate)
print("The Final Tax amount should be paid is: ",Tax)

#QUES. 3
# take input from student 
# and make list
SID = int(input("Enter your StudentID:"))
Name = input("enter your Name:")
Gender = input("enter your Gender M/F/U:")
if(Gender == 'M'):
 Gender = "Male"
elif(Gender == 'F'):
 Gender = "Female"
else:
 Gender = "unknown"
 
Course = input("enter your course :")
CGPA = float(input("enter your CGPA:"))
# store the value from user and making list of all the information
Student = [SID, Name, Gender, Course, CGPA]
# now we printing the details
print(Student)

#QUES 4
# take the marks of five students then arrange in list then sort in and get sorted output
marks1 = int(input("Marks of 1st student : "))
marks2 = int(input("Marks of 2nd student : "))
marks3 = int(input("Marks of 3rd student : "))
marks4 = int(input("Marks of 4th student : "))
marks5 = int(input("Marks of 5th student : "))
SortedMarks = [marks1, marks2, marks3, marks4, marks5]
SortedMarks.sort() # to sort the list in a order.
print(SortedMarks)

#QUES 5
#a) 
#create a list of colors
color=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print(color)
# (a) Python program to print a specified list after removing 4th element.
color.pop(3) # 3 is index to 4th element of color list
 print("output of part a is:")
print(color)

#b) 
# (b) Remove ‘Black’ and ‘Pink’ from the list and replace them with ‘Purple’.
# Do that in one line code.
# index of black is 3 and index of pink is 4
print("output of part b is:") 
color=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color[3:5]=["Purple"] #replace 
print(color)
