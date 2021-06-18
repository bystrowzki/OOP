class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lectures(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached and grade <= 10:
            lecturer.grades += [grade]
        else:
            return 'Ошибка'

    def get_avg_grade(self):
        summa = 0
        count = 0
        for grades in self.grades.values():
            summa += sum(grades)
            count += len(grades)
        return round(summa/count, 2)

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nГендер: {self.gender}\nКурсы в процессе: {self.courses_in_progress}\n' \
              f'Законченные курсы: {self.finished_courses}\nСредняя оценка за ДЗ: {self.get_avg_grade()}\n'
        return res

    def compare_avg_grade(self, student):
        if self.get_avg_grade() > student.get_avg_grade():
            res = f'{self.name} {self.surname} ({str(self.get_avg_grade())}) учится лучше, чем {student.name} {student.surname} ({str(student.get_avg_grade())})\n'
            return res
        elif self.get_avg_grade() < student.get_avg_grade():
            res = f'{self.name} {self.surname} ({str(self.get_avg_grade())}) учится хуже, чем {student.name} {student.surname} ({str(student.get_avg_grade())})\n'
            return res
        elif self.get_avg_grade() == student.get_avg_grade():
            res = f'{self.name} {self.surname} ({str(self.get_avg_grade())}) учится также, как {student.name} {student.surname} ({str(student.get_avg_grade())})\n'
            return res


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = []

    def avg_mentor_grade(self):
        res = sum(self.grades)/len(self.grades)
        return res

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.avg_mentor_grade()}\n'
        return res

    def compare_avg_grades(self, lecturer):
        if self.avg_mentor_grade() > lecturer.avg_mentor_grade():
            res = f'{self.name} {self.surname} ({str(self.avg_mentor_grade())}) ведёт лекции лучше, чем {lecturer.name} {lecturer.surname} ({str(lecturer.avg_mentor_grade())})\n'
            return res
        elif self.avg_mentor_grade() < lecturer.avg_mentor_grade():
            res = f'{self.name} {self.surname} ({str(self.avg_mentor_grade())}) ведёт лекции хуже, чем {lecturer.name} {lecturer.surname} ({str(lecturer.avg_mentor_grade())})\n'
            return res
        elif self.avg_mentor_grade() == lecturer.avg_mentor_grade():
            res = f'{self.name} {self.surname} ({str(self.avg_mentor_grade())}) ведёт лекции также хорошо, как {lecturer.name} {lecturer.surname} ({str(lecturer.avg_mentor_grade())})\n'
            return res


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\n'
        return res


def get_avg_lect_grade(lecturers_list):
    total_sum = 0
    for lecturer in lecturers_list:
        total_sum += sum(lecturer.grades) / len(lecturer.grades)
    return total_sum/len(lecturers_list)

def get_avg_hw_grade(student_list, course):
    summa = 0
    for student in student_list:
        for c, grades in student.grades.items():
            if c == course:
                summa += sum(grades) / len(grades)
    return round(summa/len(student_list), 2)


best_student = Student('Ruoy', 'Eman', 'non-binary')
best_student.courses_in_progress += ['Python']
best_student.finished_courses += ['Введение в программирование']
some_student = Student('Sasha', 'Bystrovskaya', 'woman')
some_student.courses_in_progress += ['Python']
some_student.finished_courses += ['Введение в программирование']

cool_mentor = Lecturer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
second_mentor = Lecturer('New', 'Lecturer')
second_mentor.courses_attached += ['Python']

new_mentor = Reviewer('Best', 'Mentor')
new_mentor.courses_attached += ['Python']
worst_mentor = Reviewer('Nice', 'Guy')
worst_mentor.courses_attached += ['Python']

best_student.rate_lectures(cool_mentor, 'Python', 10)
some_student.rate_lectures(cool_mentor, 'Python', 8)
some_student.rate_lectures(second_mentor, 'Python', 9)
new_mentor.rate_hw(some_student, 'Python', 7)
worst_mentor.rate_hw(best_student, 'Python', 6)

print(cool_mentor.grades)
print(some_student.grades)
print(best_student.__str__())
print(cool_mentor.__str__())
print(worst_mentor.__str__())
print(cool_mentor.compare_avg_grades(second_mentor))
print(best_student.compare_avg_grade(some_student))
print(get_avg_hw_grade([best_student, some_student], 'Python'))
print(get_avg_lect_grade([cool_mentor, second_mentor]))