class StudentManager:
    def __init__(self):

        def add_student(self, name: str, grades: list):
            ifname in self.students:
            raiser ValueError(f"Student{name} already exists.")
            if not all(isinstance(grade, (int,float))for grade in grade in grades):
                raise ValueError("Grades must be a list of numbers.")
                self.students[name] = grades
                
        def get_average(self,name: str) -> float:
            if name not in self.students:
                raise ValueError(f"Student{name}does not exists")
                return sum(self.students[name]/len(self.students[name]))
        
        def is_passed(self. name:str, passing_grade: float = 6.0) ->bool:
            average = self.get_average(name)
            return average >= passing_grade

import unittest

class TestStudentManager(unittest.TestCase):
    def setup(self):
    #configuração inicial para cada teste.
    self.manager = StudentManager()

    def test_add_student(self):
        self.manager.add_student("Alice",[8.0,7.5,9.0])
        self.assertIn("Alice", self.manager.students)

    def test_add_student_existing(self):
        self.manager.add_student("Alice",[8.0,7.5,9.0])
        with self.assertInRaises(ValueError):
            self.manager.add_student("Alice",[6.0,7.0])
