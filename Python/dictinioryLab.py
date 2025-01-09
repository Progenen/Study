School = {}
countClasses = 4
countChangeClasses = 2
i = 0
j = 0

while i <= countClasses:
    print("Введите название класса:")
    nameClass = str(input())
    print("Введит кол-во учеников")
    studentsCount = int(input())


    School[nameClass] = studentsCount
    i+=1

while j <= countChangeClasses:
    print("Введите название изменяемого класса:");
    nameClassChange = str(input())
    print("Введите новое кол-во учеников:")
    studentsCountChange = int(input())

    School[nameClassChange] = studentsCountChange
    
    j+=1

print(School)


