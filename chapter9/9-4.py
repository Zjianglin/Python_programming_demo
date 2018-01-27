'''
9–4. 文件访问. 写一个逐页显示文本文件的程序. 提示输入一个文件名, 每次显示文本
文件的 25 行, 暂停并向用户提示"按任意键继续.", 按键后继续执行.
'''

def main():
    fname = input('Enter a file to display: ')
    
    with open(fname, encoding='utf-8') as fin:
        start = 0
        for i, line in enumerate(fin):
            if i - start > 24:
                input('Press any key to continue...')
                start = i
            print('line {} :'.format(i + 1), line)
    
    print('****END***')

if __name__ == '__main__':
    main()
    