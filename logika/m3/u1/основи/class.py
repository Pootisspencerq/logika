class Student ():
    def __init__(self, surname, name, grade):
        self.surname = surname
        self.name = name
        self.grade = grade
students = []      
        
with open ('class.txt', 'r',encoding="utf-8") as file:
    for  line in file:
        data =line.split(' ')
        obj =Student (data[0], data[1], int(data[2]))
        students.append(obj)
        
for student in students:
     if student.grade == 5:
        print(student.surname)