# Домашняя работа по уроку "Пространство имен.

def test_function():

    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()


test_function()
# inner_function()# - вызов этой функции из глобального пространства приводит к ошибке, потому что inner_function -
# находится в локальном пространстве функции test_function.
