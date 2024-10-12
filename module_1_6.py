my_dict={'a':1,'b':2,'c':3}
print(my_dict)
print('выбрано: ',my_dict['b'])#Existing value

print(my_dict.get('d','Не найден'))#Not existing value
my_dict.update(d = 4,e = 5)
print('новый:',my_dict)
a=my_dict.pop('c')
print('извлечено:',a)
print(my_dict)

my_set ={'a','b','c',1,2,3,4,5,3,4,5}
print(my_set )
d=('z',58,2)
my_set .update(d)
print(my_set )
print(my_set.discard(2))
print(my_set.remove(4))
print(my_set )
