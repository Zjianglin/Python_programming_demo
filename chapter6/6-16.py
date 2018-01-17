'''
6-16.矩阵。处理矩阵M和N的加和乘操作。
'''

def matrix_add(mtr1, mtr2):
    '''
    mtr1 and mtr2 must be same size: m x n
    '''
    if not (mtr1 and mtr2):
        raise ValueError('Input matrix cannot be None')
    size = lambda m: (len(m), len(m[0]))
    m, n = size(mtr1)
    if (m, n) != size(mtr2):
        raise ValueError('Two matrixes must be same size')

    matrix = [[0.0] * n for i in range(m) ]
    for i in range(m):
        for j in range(n):
            matrix[i][j] = mtr1[i][j] + mtr2[i][j]
    
    return matrix

def matrix_mul(mtr1, mtr2):
    if not (mtr1 and mtr2):
        raise ValueError('Input matrix cannot be None')
    size = lambda m: (len(m), len(m[0]))
    m1, n1 = size(mtr1)
    m2, n2 = size(mtr2)
    if n1 != m2:
        raise ValueError('the columns of matrix1 should be equal to the row of matrix2')
    C = [[0.0] * n2 for i in range(m1) ]
    for i in range(m1):
        for j in range(n2):
            for k in range(n1):
                C[i][j] += mtr1[i][k] * mtr2[k][j]
    
    return C

def pretty_print(M):
    if not M:
        return
    print("[{}]".format(',\n'.join(
        str(r) for r in M
    )))

def main():
    m1 = [[0, 0], [2, 1]]
    m2 = [[1, 2], [0, 0]]
    pretty_print(matrix_add(m1, m2))
    pretty_print(matrix_mul(m1, m2))

    m1 = [[i for i in range(3)] for j in range(4)]
    m2 = [[i for i in range(5)] for j in range(3)]
    pretty_print(matrix_mul(m1, m2))


if __name__ == '__main__':
    main()
        
            
