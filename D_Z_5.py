n, m, value = input('Введите число n: '), input('Введите число m: '), input('Введите число значение3: ')
matrix = []
def get_matrix(n, m, value):
    for i in range(0, int(n)):
        matrix.append([])
        for j in range(0, int(m)):
            matrix[i].append(value)
    return matrix
#get_matrix(n, m, value)
print(get_matrix(n, m, value))
