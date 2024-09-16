my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
print(my_list)
print('if a<=0, stop.')
value = 0
while len(my_list) > value:
    if my_list[value] > 0:
        print(my_list[value])
    if my_list[value] < 0:
        break
    value += 1


