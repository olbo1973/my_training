first=input('введите число: ')
second=input('введите число: ')
third=input('введите число: ')
if first == second and first==third:
    print(3)

elif first == second or first == third or second ==third:
    print(2)

else:
    print(0)