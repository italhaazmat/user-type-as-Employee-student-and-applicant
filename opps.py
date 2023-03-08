class Person:
    def _init_(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def _init_(self, name, age, grade):
        super()._init_(name, age)
        self.grade = grade

class Employee(Person):
    def _init_(self, name, age, salary):
        super()._init_(name, age)
        self.salary = salary

class Teacher(Employee):
    def _init_(self, name, age, salary, subject):
        super()._init_(name, age, salary)
        self.subject = subject

print("What type of person are you? Please enter student, employee, or teacher.")
person_type = input()

if person_type == "student":
    print("Please enter your name:")
    name = input()
    print("Please enter your age:")
    age = int(input())
    print("Please enter your grade:")
    grade = int(input())
    student = Student(name, age, grade)
    print(f"Welcome, {student.name}! You are a student in grade {student.grade}.")
elif person_type == "employee":
    print("Please enter your name:")
    name = input()
    print("Please enter your age:")
    age = int(input())
    print("Please enter your salary:")
    salary = float(input())
    employee = Employee(name, age, salary)
    print(f"Welcome, {employee.name}! You are an employee with a salary of {employee.salary}.")
elif person_type == "teacher":
    print("Please enter your name:")
    name = input()
    print("Please enter your age:")
    age = int(input())
    print("Please enter your salary:")
    salary = float(input())
    print("Please enter your subject:")
    subject = input()
    teacher = Teacher(name, age, salary, subject)
    print(f"Welcome, {teacher.name}! You are a teacher of {teacher.subject} with a salary of {teacher.salary}.")
else:
    print("Invalid input. Please enter student, employee, or teacher.")