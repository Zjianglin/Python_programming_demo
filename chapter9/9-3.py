'''
9–3. 文件信息. 提示输入一个文件名, 然后显示这个文本文件的总行数.
'''

def lines_of(fname):
    with open(fname, encoding='utf-8') as fin:
        return sum(1 for line in fin)

def main():
    fname = input('Enter a file name: ')
    print('The number of lines of [{}] is {}'.format(fname, lines_of(fname)))

if __name__ == '__main__':
    main()
    