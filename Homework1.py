class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def lecturers_grade(self, lecturer, course, grade):
            if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached \
                    and course in self.courses_in_progress \
                    and 1 <= grade <= 10:
                if course not in lecturer.grade_from_students:
                    lecturer.grade_from_students[course] = [grade]
                else:
                    lecturer.grade_from_students[course] += [grade]
            else:
                return 'Ошибка'

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    grade_from_students = {}

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
