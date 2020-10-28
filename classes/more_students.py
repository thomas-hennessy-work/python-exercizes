class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.class_ = "student"

    def test_score(self, first_score, second_score, third_score):
        self.score = ((first_score + second_score + third_score)/3)

    def graduation(self):
        self.class_ = "graduate"

John = Student("John", 22)

John.test_score(65, 65, 80)
print(John.score)

print(John.class_)
John.graduation()
print(John.class_)