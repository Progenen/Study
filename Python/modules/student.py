
from collections import namedtuple

class Student:
    def __init__(self, fullName, course, age, address, phone, speciality ):
        self.name = fullName
        self.course = course
        self.age = age
        self.address = address
        self.phone = phone
        self.speciality = speciality

    
    def get_info(self):
        stud = namedtuple('Stud', 'name, course, age, address, phone, speciality')
        return stud(name=self.name, course=self.course, age=self.age, address=self.address, phone=self.phone, speciality=self.speciality)
    
    def set_info(self, fullName, course, age, address, phone, speciality):
        self.name = fullName
        self.course = course
        self.age = age
        self.address = address
        self.phone = phone
        self.speciality = speciality

    def get_name(self): 
        return self.name