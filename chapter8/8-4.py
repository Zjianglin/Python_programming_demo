'''
8–4. 素数. 我们在本章已经给出了一些代码来确定一个数字的最大约数或者它是否是一个
素数. 请把相关代码转换为一个返回值为布尔值的函数，函数名为 isprime() . 如果输入的是一个
素数, 那么返回 True , 否则返回 False .
'''

def isprime(num):
    i = 2;
    while i * i <= num:
        if num % i == 0:
            return False
        i += 2 if i > 2 else 1
    return (num > 1)

def main():
    for n in range(2, 30, 3):
        if isprime(n):
            print(n, ' is a prime')
        else:
            print(n, ' is not a prime')
    print(10**20, 'is a prime? ', isprime(10**20))

if __name__ == '__main__':
    main()
    