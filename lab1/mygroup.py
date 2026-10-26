# Список студентов
groupmates = [
    {
        "name": "Марина",
        "surname": "Иванова",
        "exams": ["Информатика", "ЭЗИС", "Web"],
        "marks": [3, 4, 5]
    },
    {
        "name": "Пётр",
        "surname": "Сидоров",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [3, 3, 5]
    },
    {
        "name": "Вася",
        "surname": "Колобков",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [5, 4, 4]
    },
    {
        "name": "Анна",
        "surname": "Козлова",
        "exams": ["Математика", "Физика", "Информатика"],
        "marks": [5, 4, 5]
    },
    {
        "name": "Дмитрий",
        "surname": "Соколов",
        "exams": ["История", "Право", "Экономика"],
        "marks": [3, 4, 3]
    }
]

# Функция вывода всех студентов
def print_students(students):
    print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(30), u"Оценки".ljust(20))
    for student in students:
        print(student["name"].ljust(15),
              student["surname"].ljust(10),
              str(student["exams"]).ljust(30),
              str(student["marks"]).ljust(20))

# Функция фильтрации
def filter_by_average_grade(students, min_grade):
    print(f"\n--- Студенты со средним баллом выше {min_grade} ---")
    found = False
    for student in students:
        avg_grade = sum(student["marks"]) / len(student["marks"])
        if avg_grade > min_grade:
            print(f"{student['name']} {student['surname']} — Средний балл: {avg_grade:.2f}")
            found = True
    if not found:
        print("Таких студентов нет.")

# Вызов функции вывода
print("Все студенты:")
print_students(groupmates)

# Запрос ввода у пользователя
try:
    user_input = float(input("\nВведите минимальный средний балл для фильтрации (например, 4.0): "))
    filter_by_average_grade(groupmates, user_input)
except ValueError:
    print("Ошибка! Пожалуйста, введите число (например, 4.5).")