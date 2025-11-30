# class Student:
#     amout_of_students = 0
#     def __init__(self, height=160):
#         self.height = height
#         Student.amout_of_students += 1
# nick = Student()
# kate = Student(height=170)
# print(nick.amout_of_students)
# print(kate.amout_of_students)

# class Student:
#     def __init__(self):
#         self.height = 170
#     height = 160
#     def printer(self):
#         print(self.height)
# nick = Student()
# nick.printer()

# class Student():
#     amout_of_student = 0
#     def __init__(self, height = 160):
#         self.height = height
#         Student.amout_of_student +=1
#     def grow(self, height = 170):
#         self.height += height
# yaroslav = Student()
# kate = Student(height=170)
# yaroslav.grow(height = 15)
# print(kate.height)
# print(yaroslav.height)

# class Student:
#     def __init__(self, name=None):
#         self.name = name
#     def __str__(self):
#         return f"I am a student. My name is {self.name}."
# nick = Student(name = "Nick")
# print(nick)

 # class Student:
 #     def __init__(self, name=None):
 #       self.name = name
 #    def __del__(self):
 #        print("training is over")
 # nick = Student()

class Student:
    def __init__(self, name=None, height=160):
        self.name = name
        self.height = height
    def __bool__(self):
        return self.name != None
    def __len__(self):
        return self.height
nick = Student()
print(nick.__len__())
print(nick.__bool__())
print(len(nick))
print(bool(nick))