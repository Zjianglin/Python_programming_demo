'''
8–9. Fibonacci 数列. Fibonacci 数列形如 1, 1, 2, 3, 5, 8, 13, 21, 等等. 也就是说,
下一个值是序列中前两个值之和. 写一个函数, 给定 N , 返回第 N 个 Fibonacci 数字. 例如, 第
1 个 Fibonacci 数字是 1 , 第 6 个是 8 .
'''

def Fib(n):
    a, b = 0, 1
    for i in range(n - 1):
        a, b = b, a + b
    
    return b

def fib(n):
    a, b = 0, 1
    for i in range(n):
        yield b
        a, b = b, a + b
    return 'Done'

def main():
    print(list(fib(9)))

    for i in range(1, 10):
        print('the {}th fibonacci number is {}'.format(i, Fib(i)))

if __name__ == '__main__':
    main()
    