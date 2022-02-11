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
