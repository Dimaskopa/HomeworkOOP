def count_grades(grade):
    count = 0
    count_courses = 0
    for key, value in grade.items():
        count += len(value) / sum(value)
        count_courses += 1
    return count_courses/count

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
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\n' \
               f'Средняя оценка за домашнее задание: {count_grades(self.grades)}\n' \
               f'Курсы в процессе изучения: {", ".join(map(str, self.courses_in_progress))}\n' \
               f'Завершенные курсы: {", ".join(map(str, self.finished_courses))}'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    grade_from_students = {}

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\n' \
               f'Средняя оценка за лекции: {count_grades(self.grade_from_students)}'

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'
