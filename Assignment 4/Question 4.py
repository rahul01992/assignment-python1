print("Answere number 4")


class Student:
    def __init__(self, student, roll_no):
        self.name = student
        self.roll_no = roll_no

    def __del__(self):
        print("Object deleted")


# creating object
student1 = Student("Onkar",21103123)
print("Object created")
print(f"The name of the student it {student1.name} and SID is {student1.roll_no}.")# printing the assigned values
del student1# deleting object
