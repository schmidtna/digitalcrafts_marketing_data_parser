lottery_player_dict = {
    'name': 'Rolf',
    'numbers': (5, 9, 12, 2, 1, 21)
}

class LotteryPlayer:
    def __init__(self, name):
        self.name = name
        self.numbers = (5, 9, 12, 2, 1, 21)

    def total(self):
        return sum(self.numbers)

player_one = LotteryPlayer("Rolf")
player_one.numbers = (1, 2, 3, 6, 7, 8)
player_two = LotteryPlayer("John")

#print(player.name)
#print(player.numbers)
#print(player.total())

##

class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.grades = []

    def grade_average(self):
        return sum(self.grades) / len(self.grades)

    @classmethod
    def go_to_school(cls):
        print("I'm going to school.")

    @staticmethod
    def static_to_school()
        print("Someone's going to school.")


anna = Student("Anna", "MIT")
anna.grades.append(56)
anna.grades.append(71)

print(anna.grade_average())
anna.go_to_school()

Student.static_to_school()