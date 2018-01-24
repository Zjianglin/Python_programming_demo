'''
8–11. 文本处理. 要求输入一个姓名列表，输入格式是“Last Name, First Name,” 即 姓,
逗号, 名. 编写程序处理输入, 如果用户输入错误, 比如“First Name Last Name,” , 请纠正这
些错误, 并通知用户. 同时你还需要记录输入错误次数. 当用户输入结束后, 给列表排序, 然后以
"姓 , 名" 的顺序显示.
'''

def main():
    names = []
    times = 0
    N = int(input('Enter total number of names: '))
    print('Format should be Last, First.')

    for i in range(N):
        while True:
            name = input('Please enter name {}: '.format(i)).strip()
            if len(name.split(',')) != 2:
                print('Wrong format...should be Last, First')
                times += 1
                print('You have done this {} time(s) already. Fixing input...'.format(times))
            else:
                break
        names.append(name)
    
    print('\nThe sorted list (by last name) is:')
    for name in sorted(names, key=lambda n: n.split(',')[0]):
        print(name)

if __name__ == '__main__':
    main()
    