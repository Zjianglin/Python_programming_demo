# -*- coding:utf-8 -*-
# python 3

'''
6.19 多列输出。有任意项的序列或者其他容器，把它们等距离分列显示。由调用者提供
数据和输出格式。例如，如果你传入100个项并定义3列输出，按照需要的模式显示这些
数据。这种情况下，应该是两列显示33个项，最后一列显示34个。你可以让用户来选择
水平排序或者垂直排序。
'''


def fp_list(li, cols, sort=0):
    '''
    print list with specific format.
    cols specifies how many columns for the list to be printed.
    sort = 0 for horizontal sort, 1 for vertical sort.
    '''
    if cols > len(li):
        raise ValueError('cols should <= length of input container')
    L = sorted(li)

    if sort:
        #vertical sort
        row = len(L) // cols
        for i in range(row):
            for j in range(cols):
                print('{:4}'.format(L[j * row + i]), end='\t')
            print()
        padding = '    \t' * (cols - 1)

        
        for i in range(len(L) % cols):
            print(padding + '{:4}'.format(L[row * cols + i]))
    else:
        #horizontal sort
        for i in range(len(L)):
            print('{:4}'.format(L[i]), end='\t')
            if not ((i + 1) % cols):
                print()
    
    print()

def main():
    data = list(range(1, 101))
    '''
    fp_list(data, 3, sort=0)
    fp_list(data, 3, sort=1)

    '''
    print('Input the number of columns:')
    cols = int(input(''))
    while True:
        print('{:*^20}'.format('Display Format'))
        print('0 for horizontal sort')
        print('1 for vertical sort')
        print('2 for quit\n')

        print('Please input diplay format:')
        op = int(input())
        if op == 0:
            fp_list(data, cols, sort=0)
        elif op == 1:
            fp_list(data, cols, sort=1)
        else:
            break
    
if __name__ == '__main__':
    main()
    
