value = 2
m = 2
n = 2

def get_matrix(n, m, value):
    matrix = []
    list = []
    for i in range(0, n):
        for j in range(0, m):
            list.append(value)
            print('list', i, list)
        matrix.append(list)
        list = []
    return matrix

print('matrix:', get_matrix(n,m, value))
