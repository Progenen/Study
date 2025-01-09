# Ввод списка студентов с терминала
students = []
num_students = int(input("Введите количество студентов: "))

for _ in range(num_students):
    name = input("Введите имя студента: ")
    age = int(input(f"Введите возраст студента {name}: "))
    height = float(input(f"Введите рост студента {name} (в см): "))
    weight = float(input(f"Введите вес студента {name} (в кг): "))
    pay = float(input(f"Введите расходы студента {name} (в тенге): "))
    students.append({"name": name, "age": age, "height": height, "weight": weight, "pay": pay})

print("\nСписок студентов:")
for student in students:
    print(f"Имя: {student['name']}, Возраст: {student['age']}, Рост: {student['height']} см, Вес: {student['weight']} кг, Расходы: {student['pay']} тенге")

total_pay = sum(student["pay"] for student in students)
print(f"\nОбщая сумма расходов студентов: {total_pay} тенге")

min_height = float(input("\nВведите минимальный рост для фильтрации (см): "))
max_weight = float(input("Введите максимальный вес для фильтрации (кг): "))

filtered_students = [
    student for student in students
    if student["height"] > min_height and student["weight"] < max_weight
]

print("\nСтуденты, соответствующие критериям:")
if filtered_students:
    for student in filtered_students:
        print(f"Имя: {student['name']}, Рост: {student['height']} см, Вес: {student['weight']} кг")
else:
    print("Нет студентов, соответствующих критериям.")