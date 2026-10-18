"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""




from copy import copy, deepcopy


# TODO 1: Create a parent class with a class variable,
# a name, an age, and a method to display the information.
class ParentClass:
    school = "UMGC"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(self.name, self.age)


# TODO 2: Create a child class that inherits from the parent.
# Add student information, a new method, and change display_info.
class ChildClass(ParentClass):
    student_type = "Undergraduate"

    def __init__(self, name, age, student_id, major):
        super().__init__(name, age)
        self.student_id = student_id
        self.major = major
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)

    # Display the student information instead of just name and age.
    def display_info(self):
        print(self.name, self.age, self.student_id, self.major)
        print(self.courses)

    # TODO 6: My added feature counts the student's courses.
    def count_courses(self):
        print("Number of courses:", len(self.courses))


# TODO 3: Show the difference between class and object variables.
def demonstrate_namespaces():
    print("\n=== Namespaces ===")

    # Create two students.
    s1 = ChildClass("Alex", 20, "101", "Computer Science")
    s2 = ChildClass("Ben", 22, "102", "Cybersecurity")

    # Access the same class variable two different ways.
    print(ChildClass.student_type)
    print(s1.student_type)

    # Add a new attribute to only the first student.
    s1.hobby = "Gaming"

    # Show what is stored in each student and the class.
    print(s1.__dict__)
    print(s2.__dict__)
    print(ChildClass.__dict__)


# TODO 4: Show how shallow and deep copies work.
def demonstrate_copying():
    print("\n=== Copying ===")

    # Make a list that contains other lists.
    original = [[1, 2], [3, 4]]

    # Make one shallow copy and one deep copy.
    shallow = copy(original)
    deep = deepcopy(original)

    # Change a number in the original list.
    original[0][0] = 9

    # The shallow copy also changes because it shares the inner lists.
    # The deep copy stays the same because it has its own inner lists.
    print("Original:", original)
    print("Shallow:", shallow)
    print("Deep:", deep)


# TODO 5: Create objects and test the classes and methods.
def main():
    print("=== Unit 1 OOP Assignment ===")

    # Create a person and display their information.
    person = ParentClass("Cleo", 45)
    person.display_info()

    # Create a student, add courses, and display the info.
    student = ChildClass("Dana", 22, "123", "Computer Science")
    student.add_course("Python")
    student.add_course("Java")
    student.display_info()

    # Test my aded feature.
    student.count_courses()

    # Run the namespace and copying examples.
    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()
