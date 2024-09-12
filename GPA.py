grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
#print(type(grades))
sorted_list = list(students)
sorted_list.sort()
#sorted_set = set(sorted_list)
#numbers = [4, 8, 6, 5, 3, 2]
#average = sum(numbers) / len(numbers)
#print(average)
print(sorted_list)
grades1 = [grades[0] , grades[1] , grades[2] , grades[3] , grades[4]]
print(grades1)
grades1_sm= [sum(grades1[0])/len(grades1[0]),sum(grades1[1])/len(grades1[1]),sum(grades1[2])/len(grades1[2]),
             sum(grades1[3])/len(grades1[3]),sum(grades1[4])/len(grades1[4])]
#print(grades1_sm)
dict= dict(zip(sorted_list, grades1_sm))
#{sorted_list[0],grades1_sm[0],sorted_list[1],grades1_sm[1],sorted_list[2],grades1_sm[2],
           #sorted_list[3],grades1_sm[3], sorted_list[4],grades1_sm[4]}
print(dict)


