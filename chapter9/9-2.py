'''
9–2. 文件访问. 提示输入数字 N 和文件 F, 然后显示文件 F 的前 N 行.
'''

def main():
    fname = input('Enter file to display: ')
    N = int(input('Enter the numer of lines to display: '))
    try:
        print('\n***the first {} lines of file: {}'.format(N, fname))
        with open(fname) as fin:
            for i, line in enumerate(fin):
                if (i + 1) > N:
                    break
                else:
                    print('line {} :'.format(i), line)
    except Exception as err:
        print(err)

if __name__ == '__main__':
    main()
    