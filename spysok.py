ata = """
Иванов О. 4
Петров И. 3
Дмитриев Н. 2
Смирнова О. 4
Керченских В. 5
Котов Д. 2
Бирюкова Н. 5
Данилов П. 3
Аранских В. 5
Лемонов Ю. 2
Олегова К. 4
"""

def find_excellent_students(data):
    excellent_students = []

    
    lines = data.strip().split('\n')

    for line in lines:
        
        parts = line.split()
        
        
        grade = int(parts[-1])

        
        if grade > 4:
            excellent_students.append(line)

    return excellent_students

excellent_students = find_excellent_students(data)


for student in excellent_students:
    print(student)
