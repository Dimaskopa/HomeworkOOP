#Функция для подсчетов средней оценки:
def count_grades(grade):
    count = 0
    count_courses = 0
    for key, value in grade.items():
        count += len(value) / sum(value)
        count_courses += 1
    return count_courses/count
def count_grade_course(grade):
    count = 0
    for i in grade.values():
        count += sum(i)

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

#Метод для выставления оценок лекторам:
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

#Переопределение вывода
    def __str__(self):
        self.avg_grade = round(count_grades(self.grades), 2)
        return f'Имя: {self.name}\nФамилия: {self.surname}\n' \
               f'Средняя оценка за домашнее задание: {round(count_grades(self.grades), 2)}\n' \
               f'Курсы в процессе изучения: {", ".join(map(str, self.courses_in_progress))}\n' \
               f'Завершенные курсы: {", ".join(map(str, self.finished_courses))}'

# Сравнение студентов по средней оценки
    def __lt__(self, other):
        return self.avg_grade < other.avg_grade


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grade_from_students = {}
        self.courses_attached = []

#Переопределение вывода
    def __str__(self):
        self.avg_grade = round(count_grades(self.grade_from_students), 2)
        return f'Имя: {self.name}\nФамилия: {self.surname}\n' \
               f'Средняя оценка за лекции: {round(count_grades(self.grade_from_students), 2)}'

#Сравнение лекторов по средней оценки
    def __lt__(self, other):
        return self.avg_grade < other.avg_grade

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

#Функция для подсчета среднего бала среди всех студентов по конкретному предмету
def student_avg_course(course, *args):
    sum_count = 0
    average_grade = 0
    for i in args:
        sum_count += sum(i.grades[course])/len(i.grades[course])
        average_grade += 1
    print(f'Средняя оценка за курс {course} у студентов: {round( sum_count / average_grade, 2)}')

#Функция для подсчета среднего бала среди всех лекторов по конкретному предмету
def lecturer_avg_course(course, *args):
    sum_count = 0
    average_grade = 0
    for i in args:
        sum_count += sum(i.grade_from_students[course])/len(i.grade_from_students[course])
        average_grade += 1
    print(f'Средняя оценка за курс {course} у лекторов: {round( sum_count / average_grade, 2)}')

#Добавление Рецензента:
dima = Reviewer('Dima', 'Medvedev')
dima.courses_attached = ['Python', 'Git']

#Добавление студентов и курсов
lena = Student('Elena', 'Khodchenko', 'Female')
lena.finished_courses =['Введение в программирование']
lena.courses_in_progress = ['Python', 'Git']
sonia = Student('Sofia', 'Khodchenko', 'Female')
sonia.courses_in_progress = ['Python', 'Git']

#Добавление лекторов и курсов
misha = Lecturer('Misha', 'Ivanov')
misha.courses_attached = ['Python', 'Git']
anton = Lecturer('Anton', 'Ivanov')
anton.courses_attached = ['Python', 'Git']

#Рецензент выставляет оценки студентам
dima.rate_hw(lena, 'Python', 5)
dima.rate_hw(lena, 'Python', 9)
dima.rate_hw(lena, 'Python', 8)
dima.rate_hw(sonia, 'Python', 8)
dima.rate_hw(sonia, 'Python', 7)

#Студенты выставляют оценки за лекции
lena.lecturers_grade(misha, 'Python', 5)
lena.lecturers_grade(misha, 'Python', 5)
lena.lecturers_grade(misha, 'Python', 3)
lena.lecturers_grade(misha, 'Python', 2)
lena.lecturers_grade(anton, 'Python', 4)
lena.lecturers_grade(anton, 'Python', 4)
lena.lecturers_grade(anton, 'Python', 9)

#Информация о студентах
print(lena)
print("-------------------")
print(sonia)
print("-------------------")

#Информация о лекторах
print(misha)
print("-------------------")
print(anton)
print("-------------------")

#Информация о резензенте
print(dima)
print("-------------------")

#Средняя оценка у всех студентов за курс Python
student_avg_course('Python', lena, sonia)
print("-------------------")

#Средняя оценка у всех лекторов за курс Python
lecturer_avg_course('Python', anton, misha)
print("-------------------")

#Сравнение по средним оценка за домашние задания у студентов
if lena > sonia:
    print(f'У {lena.name} {lena.surname} средний бал за домашнее задание на {round(lena.avg_grade - sonia.avg_grade, 2)}  '
          f'выше чем у {sonia.name} {sonia.surname}')
else:
    print(
        f'У {lena.name} {lena.surname} средний бал за домашнее задание на {round(sonia.avg_grade - lena.avg_grade, 2)}  '
        f'ниже чем у {sonia.name} {sonia.surname}')
print("-------------------")

#Сравнение по средним оценка за домашние задания у лекторов
if anton > misha:
    print(f'У {anton.name} {anton.surname} средний бал за домашнее задание на {round(anton.avg_grade - misha.avg_grade, 2)}  '
          f'выше чем у {misha.name} {misha.surname}')
else:
    print(
        f'У {anton.name} {anton.surname} средний бал за домашнее задание на {round(misha.avg_grade - anton.avg_grade, 2)}  '
        f'ниже чем у {misha.name} {misha.surname}')
print("-------------------")