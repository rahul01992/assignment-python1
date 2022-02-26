print("Answere number 5")
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
#creating employee Object
employee1 = Employee("Muskaan", 30000)
employee2 = Employee("Amir Khan", 320000)
employee3 = Employee("Virat", 90000)
#part 1st updating salary
employee1.salary = 70000
print(f"(a) The updated salary of {employee1.name} is {employee1.salary} ")
#part 1st deleting a record
print("(b) Record of Viren deleted")
del employee3
