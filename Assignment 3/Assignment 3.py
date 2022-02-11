#QUESTION1

a=str(input("ENTER ANY STRING: "))
list=a.split() #To split all the elements of string in a list
dict={} #initializing an empty dictionary
if list.__len__()==1:   #if statement will be implemented when a single word is entered
    for i in list[0]:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    print(dict)
else:
    for i in list:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    print(dict)
print("\n")

#Question 2



def Next_Date():
    list1 = [1, 3, 5, 7, 8]

    list2 = [4, 6, 9, 11]

    list3 = [2]

    list4 = [12]

    while (True):  # while loop is used so that if any wrong value is entered  then values will be entered again

        day = int(input("ENTER THE DAY: "))

        if (1 <= day <= 31):

            break

        else:

            print("Please Enter a valid day")

    while (True):  # while loop is used so that if any wrong value is entered  then values will be entered again

        month = int(input("ENTER THE MONTH OF THE YEAR: "))

        if (1 <= month <= 12):

            break

        else:

            print("Please Enter a valid month")

    while (True):  # while loop is used so that if any wrong value is entered  then values will be entered again

        year = int(input("ENTER THE YEAR: "))

        if (1800 <= year <= 2025):

            break

        else:

            print("Please Enter year from 1800 to 2025 only")

    if month in list1:

        if (day == 31):

            day = 1

            month = month + 1

            print(day, "/", month, "/", year)

        elif (day < 31):

            day += 1

            print(day, "/", month, "/", year)

        else:

            print("INVALID DATE TRY AGAIN")

            Next_Date()



    elif month in list2:

        if (day == 30):

            day = 1

            month = month + 1

            print(day, "/", month, "/", year)

        elif (day < 30):

            day += 1

            print(day, "/", month, "/", year)

        else:

            print("INVALID DATE TRY AGAIN")

            Next_Date()

    elif month in list3:

        if (year % 4 == 0):

            if (day == 29):

                day = 1

                month = month + 1

                print(day, "/", month, "/", year)

            elif (day < 29):

                day += 1

                print(day, "/", month, "/", year)

            else:

                print("INVALID DATE TRY AGAIN")

                Next_Date()

        else:

            if (day == 28):

                day = 1

                month += 1

                print(day, "/", month, "/", year)

            elif (day < 28):

                day += 1

                print(day, "/", month, "/", year)

            else:

                print("INVALID DATE TRY AGAIN")

                Next_Date()

    elif month in list4:

        if (day == 31):

            day = 1

            month = 1

            year += 1

            print(day, "/", month, "/", year)

        elif (day < 31):

            day += 1;

            print(day, "/", month, "/", year)

        else:

            print("INVALID DATE TRY AGAIN")

            Next_Date()



    else:

        print("INVALID DATE TRY AGAIN")

        Next_Date()


Next_Date()

print("\n")

#Question 3

inputlist = input('Enter elements of a list separated by space ')
user_list = inputlist.split()

print('list: ', inputlist)
# convert each item to int type
for i in range(len(user_list)):
    # convert each item to int type
    user_list[i] = int(user_list[i])
squarelist =[(user_list[i], user_list[i]**2) for i in range(len(user_list))]
print(squarelist)

#QUESTION 4
def input_point():
    p = int(input("Enter Grade Point: "))
    if p>10 or p<4:
        print("Enter between 4-10!! Try Again")
        point = input_point()
    return p
grade=input_point()
if(grade==4):
    print("Your Grade is 'D' and poor performance")
elif(grade==5):
    print("Your Grade is 'C' and Below Average performance")
elif(grade==6):
    print("Your Grade is 'C+' and Average performance")
elif(grade==7):
    print("Your Grade is 'B' and Good performance")
elif(grade==8):
    print("Your Grade is 'B+' and Very Good performance")
elif(grade==9):
    print("Your Grade is 'A' and Excellent performance")
else:
    print("Your Grade is 'A+' and outstanding performance")
print("\n")


#QUESTION5
x = 6
for i in range(x):

    for j in range(i):
        print(' ', end='')
    # printing alphabet
    for j in range(2*(x-i)-1):
        print(chr(65 + j), end='')  #ASCII value of A=65,B=66,C=67,D=68,E=69,F=70,G=71,H=72,I=73,J=74,K=75
    print()
print("\n")


#QUESTION6

sid = int(input("Enter SID: "))
name = input("Enter Name: ")
students = {sid:name}
while (1):
    choice = input("Do you want to enter another student entry(Y or N):").upper()
    if choice == 'Y':
        sid = int(input("Enter SID: "))
        name = input("Enter Name: ")
        students[sid] = name
    elif choice== 'N':
        break
    else:
        print('Enter valid word!!')

print("students details stored in the dictionary is:",students)

print("Sort dictionary using student names is :",{k:v for k,v in sorted(students.items(), key= lambda x:x[1])})

print("Sort dictionary using SID is :",{k:v for k,v in sorted(students.items())})

sid = int(input("Search Name with SID (Enter sid): "))
print("The name of student is :",students[sid])

#Question 7

def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))
no_of_terms=int(input("Enter the number of terms in series "))
if no_of_terms <= 0:     # Check if the number of terms is valid
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   sum=0
   for i in range(no_of_terms):
       print(recur_fibo(i))
       sum=sum+recur_fibo(i)
avg=float(sum/no_of_terms)
print("Avg is:",avg)

#Question 8


Set1 = {5,7,8,2,4}
Set2 = {3,7,1,3,9,5}
Set3 = {67,12,45,77}
# part a
Set_Union = Set1.union(Set2)
Set_Intersection = Set1.intersection(Set2)
Part_A_Set = Set_Union - Set_Intersection
print("a part :", Part_A_Set)
# part b(Subtracting intersection of sets taken two at a time from the Union of all three sets)
Part_B_Set = Set1.union(Set2.union(Set3)) - Set1.intersection(Set2) - Set2.intersection(Set3) - Set3.intersection(Set1)
print("b part :", Part_B_Set)
# part c(Subtracting the intersection of all three sets from the Intersection of sets taken two at a time)
Part_C_Set=((Set1.intersection(Set2)).union((Set1.intersection(Set3)).union(Set2.intersection(Set3))))-(Set1.intersection(Set2.intersection(Set3)))
print("c part :",Part_C_Set)
# part d(Excluding the numbers from 1 to 10 that are occuring in Set1)
Part_D_Set = set()
for i in range(1, 11):
    if i not in Set1:
        Part_D_Set.add(i)
print("d part :", Part_D_Set)
# part e(Excluding the numbers from 1 to 10 that are occuring in Set1, Set2 and Set3)
Part_E_Set = set()
for i in range(1, 11):
    if i not in Set1 and i not in Set2 and i not in Set3:
        Part_E_Set.add(i)
print("e part is", Part_E_Set)