'''
7–15. 编写计算器。 这个练习取材于http://math.hws.edu/ 在线免费Java 教材中的练习12.2。
编写一个程序允许用户选择两个集合:A 和B, 及运算操作符。例如，in, not in, &, |, ^, <,
<=, >, >=, ==, !=, 等. (你自己定义集合的输入语法，它们并不一定要像Java 示例中那样用方括
号括住。)解析输入的字符串，按照用户选择的运算进行操作。你写的程序代码应该比Java 版本的
该程序更简洁。
'''

def main():
    ops = set(list('&|^<>') + ['<=', '>=', '==', '!=', 'in', 'not in'])
    print('Enter set A, B and an operator. The item os set should be numbers. '
        'And operator should be one of {}'.format(ops)
    )
    A = {int(i) for i in input('Enter set A:').strip().split()}
    B = {int(i) for i in input('Enter set B:').strip().split()}

    while True:
        op = input('Enter an operator:').strip()
        if op not in ops:
            print('***Your operator is illegal. Try again!)***')
            continue
        result = eval("{} {} {}".format(A, op, B))
        print('{} {} {} is {}'.format(A, op, B, result))


if __name__ == '__main__':
    main()
    


