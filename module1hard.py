grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
# упорядочим список фамилий по алфавиту
students_list = list(students)
students_list_A = sorted(students_list)
# найдём средний балл
midl1 = sum(grades[0]) / len(grades[0])
midl2 = sum(grades[1]) / len(grades[1])
midl3 = sum(grades[2]) / len(grades[2])
midl4 = sum(grades[3]) / len(grades[3])
midl5 = sum(grades[4]) / len(grades[4])
# совместим фамилии и средние баллы
midl = [midl1, midl2, midl3, midl4, midl5]
list_1 = [students_list_A[0], midl1]
list_2 = [students_list_A[1], midl2]
list_3 = [students_list_A[2], midl3]
list_4 = [students_list_A[3], midl4]
list_5 = [students_list_A[4], midl5]
list_A = [list_1, list_2, list_3, list_4, list_5]
result = dict(list_A)
print(result)


