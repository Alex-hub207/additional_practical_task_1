grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
sorted_list_of_students = sorted(list(students))
average_score_each_student = {sorted_list_of_students[0]:sum(grades[0])/len(grades[0]),\
                              sorted_list_of_students[1]:sum(grades[1])/len(grades[1]),\
                              sorted_list_of_students[2]:sum(grades[2])/len(grades[2]),\
                              sorted_list_of_students[3]:sum(grades[3])/len(grades[3]),\
                              sorted_list_of_students[4]:sum(grades[4])/len(grades[4])}
print(average_score_each_student)

# Не понимаю, почему обратный слеш подчеркивает.
# По хорошему надо бы что-то наподобие foreach использовать.
