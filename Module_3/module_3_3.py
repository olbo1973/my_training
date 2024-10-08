# Функция с параметрами по умолчанию:
def print_params(a=1, b='строка', c=True,):
    print(a, b, c)
    print(a, b)
    print(c)
print_params()
print_params(b=25)
print_params(c=[1, 2, 3])


# Распаковка параметров:
values_list = ['Vasya', 999, 5.6]
values_dict = {'a': [1, 2, 3], 'b': 345, 'c':'qwerty' }
print_params(*values_list)
print_params(**values_dict)
# Распаковка + отдельные параметры:
values_list_2 = ['QWERTY', [40, 11, 22]]
print_params(*values_list_2, 42)