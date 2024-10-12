# module_3_5.py Самостоятельная работа по уроку "Рекурсия"
def get_multiplied_digits(number):  # Напишите функцию get_multiplied_digits и параметр number в ней.
    str_number = str(
        number)  # Создайте переменную str_number и запишите строковое представление(str) числа number в неё.
    first = int(str_number[0])  # создайте переменную first и запишите в неё первый символ из str_number в числовом представлении(int).
    if first == 0:
        first = 1
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first


result = get_multiplied_digits(40203)
print(result)
