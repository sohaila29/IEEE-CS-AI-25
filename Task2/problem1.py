def second_lowest(students):
    records =set()
    for i in students:
        records.add(i[1])

    sorted_rec = sorted(records)
    second_lowest_rec = sorted_rec[1]
    names =[]
    for i in students:
       if i[1]== second_lowest_rec:
           names.append(i[0])
    names.sort() 
    for i in names:
        print(i)      




n= int(input("enter the number: "))
students =[]
for i in range(n):
    name = input("ُenter the name: ")
    grade = float(input("enter the grade: "))
    students.append([name, grade])

second_lowest(students)
