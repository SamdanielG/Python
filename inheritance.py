class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

person1 = Person("Alice", 30)
person1.greet()

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  # Corrected typo here
        self.student_id = student_id
        
    def display_id(self):
        print(f"My student ID is {self.student_id}.")

student = Student("Bob", 20, "s12345")
student.greet()
student.display_id()
