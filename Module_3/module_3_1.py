calls = 0


# Создать функцию count_calls и изменять в ней значение переменной calls.
def count_calls():
    global calls
    calls += 1


# Создать функцию string_info с параметром string
def string_info(string):
    count_calls()  # вызвать calls
    return (len(string), string.upper(), string.lower())


# Создать функцию is_contains с двумя параметрами string и list_to_search
def is_contains(string, list_to_search):
    count_calls()
    return string.upper() in [string.upper() for s in list_to_search]


# Вывод в консоль
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBan
print(is_contains('cycle', ['recycle', 'cyclic']))  # No matches
print(calls)
