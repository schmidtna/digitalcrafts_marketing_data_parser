class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.grades = []

    def average(self):
        return sum(self.grades) / len(self.grades)

    @classmethod #will be a class of whatever class is calling it, inheriting from student/workingstudent
    def friend(cls, origin, friend_name, *args):
        return cls(friend_name, origin.school, *args)



class WorkingStudent(Student):
    def __init__(self,name, school ,salary, job_title):
        super().__init__(name, school)
        self.salary = salary
        self.job_title = job_title

anna = WorkingStudent("Anna", "Oxford", 20.00, "Student")

print(anna.salary)

friend = WorkingStudent.friend(anna, "Greg", 15.00, "Software Developer")

print(friend.name)
print(friend.school)
print(friend.salary)

