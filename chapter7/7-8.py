'''
人力资源。创建一个简单的雇员姓名和编号的程序。让用户输入一组雇员姓名和编号。
你的程序可以提供按照姓名排序输出的功能，雇员姓名显示在前面，后面是对应的雇员编号。附加
题：添加一项功能，按照雇员编号的顺序输出数据。
'''

def main():
    employees = dict()
    
    print('**' * 5)
    print('Enter employee\'s name and id, please(comma to separate).')
    print('F to finish')
    while True:
        line = [s.strip() for s in input('>>>').split()]
        if len(line) == 1 and line[0].upper() == 'F':
            break
        employees[line[0]] = line[1]
    
    print('{:*^20}'.format('Employees'))
    for n in sorted(employees.keys()):
        print(n, employees[n])
    
    print('--' * 10)
    keys = sorted(employees, key=lambda k: employees.get(k))
    print(keys)
    for k in keys:
        print(k, employees[k])

if __name__ == '__main__':
    main()
    
