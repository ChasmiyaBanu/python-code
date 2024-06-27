class Student:
    def _init_(self, name, roll_num, marks):
        self.name = name
        self.roll_num = roll_num
        self.marks = marks
        self.avg_mark = sum(marks) / len(marks)

    def _str_(self):
        return f"Name: {self.name}, Roll Number: {self.roll_num}, Average Mark: {self.avg_mark}"

def student_details():
    students = []
    for i in range(1, 2):
        print(f"Enter details for student {i}:")
        name = input("Name: ")
        roll_num = input("Roll Number: ")
        marks = []
        for j in range(3):  
            mark = float(input(f"Enter marks for Subject {j+1}: "))
            marks.append(mark)
        student = Student(name, roll_num, marks)
        students.append(student)
        print()  
    return students

def min_avg(students):
    min_avg = students[0]  
    min_avg = min_avg.avg_mark

    for student in students[1:]:
        if student.avg_mark < min_avg:
            min_avg = student.avg_mark
            min_avg = student

    print(f"Student with min avg marks:")
    print(min_avg)

def max_avg(students):
    max_avg = students[0]
    max_avg = max_avg.avg_mark

    for student in students[1:]:
        if student.avg_mark > max_avg:
            max_avg = student.avg_mark
            max_avg = student

    print(f"Student with max avg marks:")
    print(max_avg)

def rankwise_students(students):
    ranked_students = sorted(students, key=lambda student:student.avg_mark, reverse=True)
    print("Rankwise list of students based on average marks:")
    rank = 1
    for student in ranked_students:
        print(f"Rank {rank}: {student}")
        rank += 1
        if _name_ == "_main_":
            students = student_details()


min_avg(students)
max_avg(students)
rankwise_students(students)
