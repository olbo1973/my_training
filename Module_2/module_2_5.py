def get_matrix(n, m, value):
    matrix = []
    # цикл for для кол-ва строк матрицы, n повторов
    for i in range(n):
        matrix.append([])
        # цикл for для кол-ва столбцов матрицы, m повторов
        for j in range(m):
            matrix[i].append(value)
    return matrix


result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)
