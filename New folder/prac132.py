class Student:
    class_year = 2026

    def _init_(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1
student1 = Student("Spongebob", 30)
student2 = Student("Patrick", 21)

print(f"My class of {Student.class_year} has {Student.num_students} students")
print(student2.age)
print(student2.name)