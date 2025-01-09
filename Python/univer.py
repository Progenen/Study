from modules.student import Student
from collections import namedtuple

class Applicant(Student):
    def __init__(self, fullName, age, address, phone, speciality, exam_scores, chosen_university):
        super().__init__(fullName, course=0, age=age, address=address, phone=phone, speciality=speciality)
        self.exam_scores = exam_scores 
        self.chosen_university = chosen_university 

    def get_info(self):
        applicant = namedtuple('Applicant', 'name, course, age, address, phone, speciality, exam_scores, chosen_university')
        return applicant(name=self.name, course=self.course, age=self.age, address=self.address, phone=self.phone, speciality=self.speciality, exam_scores=self.exam_scores, chosen_university=self.chosen_university)

    def set_info(self, fullName, age, address, phone, speciality, exam_scores, chosen_university):
        super().set_info(fullName, course=0, age=age, address=address, phone=phone, speciality=speciality)
        self.exam_scores = exam_scores
        self.chosen_university = chosen_university

    def isPassed(self):
        return self.exam_scores > 70 if True else False
    
    def change_exam_score(self, new_score):
        self.exam_scores = new_score


appl = Applicant('John Dow', 25, "Chuvashiya", "+77777777", "IT", 69, "Zhubanov")

print(appl.get_name())