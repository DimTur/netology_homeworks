class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.avg_g = float()

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in \
                lecturer.courses_attached and course in \
                self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        grades_count = 0
        courses_in_progress_str = ', '.join(self.courses_in_progress)
        finished_courses_str = ', '.join(self.finished_courses)
        for g in self.grades:
            grades_count += len(self.grades[g])
        self.avg_g = round(sum(map(sum, self.grades.values())) / grades_count, 1)
        info_stud = f'Имя: {self.name}\n' \
                    f'Фамилия: {self.surname}\n' \
                    f'Средняя оценка за домашние задания: {self.avg_g}\n' \
                    f'Курсы в процессе изучения: {courses_in_progress_str}\n' \
                    f'Завершенные курсы: {finished_courses_str}'
        return info_stud

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Такого студента нет')
            return
        return self.avg_g < other.avg_g


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.avg_g = float()

    def __str__(self):
        grades_count = 0
        for g in self.grades:
            grades_count += len(self.grades[g])
        self.avg_g = round(sum(map(sum, self.grades.values())) / grades_count, 1)
        info_lect = f'Имя: {self.name}\n' \
                    f'Фамилия: {self.surname}\n' \
                    f'Средняя оценка за лекции: {self.avg_g}'
        return info_lect

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Такого лектора нет')
            return
        return self.avg_g < other.avg_g


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached \
                and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        info_rev = f'Имя: {self.name}\n Фамилия: {self.surname}'
        return info_rev


# Лекторы и закрепленные за ними курсы
best_lecturer_1 = Lecturer('Дима', 'Жданов')
best_lecturer_1.courses_attached += ['Python']

best_lecturer_2 = Lecturer('Иван', 'Иванов')
best_lecturer_2.courses_attached += ['Git']

best_lecturer_3 = Lecturer('Вася', 'Ишаков')
best_lecturer_3.courses_attached += ['Python']

# Проверяющие и закрепленные за ними курсы
cool_reviewer_1 = Reviewer('Гоша', 'Куценко')
cool_reviewer_1.courses_attached += ['Python']
cool_reviewer_1.courses_attached += ['Git']

cool_reviewer_2 = Reviewer('Владислав', 'Зайцев')
cool_reviewer_2.courses_attached += ['Python']
cool_reviewer_2.courses_attached += ['Git']

# Студенты, изучаемые и завершенные курсы
student_1 = Student('Вася', 'Пупкин', 'man')
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ['Введение в программирование']

student_2 = Student('Иванушка', 'Интернешенел', 'man')
student_2.courses_in_progress += ['Git']
student_2.finished_courses += ['Введение в программирование']

student_3 = Student('Деревня', 'Дураков', 'man')
student_3.courses_in_progress += ['Python']
student_3.finished_courses += ['Введение в программирование']

# Оценки лекторам за лекции
student_1.rate_hw(best_lecturer_1, 'Python', 10)
student_1.rate_hw(best_lecturer_1, 'Python', 10)
student_1.rate_hw(best_lecturer_1, 'Python', 10)

student_1.rate_hw(best_lecturer_2, 'Python', 8)
student_1.rate_hw(best_lecturer_2, 'Python', 7)
student_1.rate_hw(best_lecturer_2, 'Python', 4)

student_1.rate_hw(best_lecturer_1, 'Python', 8)
student_1.rate_hw(best_lecturer_1, 'Python', 8)
student_1.rate_hw(best_lecturer_1, 'Python', 6)

student_2.rate_hw(best_lecturer_2, 'Git', 7)
student_2.rate_hw(best_lecturer_2, 'Git', 9)
student_2.rate_hw(best_lecturer_2, 'Git', 9)

student_3.rate_hw(best_lecturer_3, 'Python', 5)
student_3.rate_hw(best_lecturer_3, 'Python', 6)
student_3.rate_hw(best_lecturer_3, 'Python', 7)

# Оценки студентам за ДЗ
cool_reviewer_1.rate_hw(student_1, 'Python', 8)
cool_reviewer_1.rate_hw(student_1, 'Python', 8)
cool_reviewer_1.rate_hw(student_1, 'Python', 7)

cool_reviewer_2.rate_hw(student_2, 'Git', 5)
cool_reviewer_2.rate_hw(student_2, 'Git', 7)
cool_reviewer_2.rate_hw(student_2, 'Git', 9)

cool_reviewer_2.rate_hw(student_3, 'Python', 10)
cool_reviewer_2.rate_hw(student_3, 'Python', 7)
cool_reviewer_2.rate_hw(student_3, 'Python', 8)

# Выводим характеристики созданных и оцененых студентов в требуемом виде
print(f'Перечень студентов:\n\n{student_1}\n\n{student_2}\n\n{student_3}')
print()
print()

# Выводим характеристики созданных и оцененых лекторов в требуемом виде
print(f'Перечень лекторов:\n\n{best_lecturer_1}\n\n{best_lecturer_2}\n\n{best_lecturer_3}')
print()
print()

# Вывод результата сравнения студентов по средним оценкам за ДЗ
print(f'Результат сравнения студентов (по средним оценкам за ДЗ:'
      f'{student_1.name} {student_1.surname} < {student_2.name} {student_2.surname} = {student_1 > student_2}')
print()

# Вывод результатf сравнения лекторов по средним оценкам за лекции
print(f'Результат сравнения лекторов (по средним оценкам за лекции): '
      f'{best_lecturer_1.name} {best_lecturer_1.surname} < {best_lecturer_2.name} {best_lecturer_2.surname} = {best_lecturer_1 > best_lecturer_2}')
print()

# Список студентов
student_list = [student_1, student_2, student_3]

# Список лекторов
lecturer_list = [best_lecturer_1, best_lecturer_2, best_lecturer_3]


# Функция подсчета средней оценки за ДЗ для студентов

def student_rating(student_list, course_name):
    sum_all = 0
    count_all = 0
    for student in student_list:
        if student.courses_in_progress == [course_name]:
            sum_all += student.avg_g
            count_all += 1
    avg_all = round(sum_all / count_all, 1)
    return avg_all


# Функция подсчета средней оценки за лекции для ректоров

def lecturer_rating(lecturer_list, course_name):
    sum_all = 0
    count_all = 0
    for lecturer in lecturer_list:
        if lecturer.courses_attached == [course_name]:
            sum_all += lecturer.avg_g
            count_all += 1
    avg_all = round(sum_all / count_all, 1)
    return avg_all

# Результат подсчета средней оценки по всем студентам для конкретного курса
print(f"Средняя оценка для всех студентов по курсу {'Python'}: {student_rating(student_list, 'Python')}")
print()

#Результат подсчета средней оценки по всем лекорам для конкретного курса
print(f"Средняя оценка для всех лекторов по курсу {'Python'}: {lecturer_rating(lecturer_list, 'Python')}")
print()