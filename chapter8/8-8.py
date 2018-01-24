'''
8–8. 阶乘. 一个数的阶乘被定义为从 1 到该数字所有数字的乘积. N 的阶乘简写为 N! .
写一个函数, 指定N, 返回 N! 的值.
'''

def factorial(num):
    ans = 1
    for i in range(2, num + 1):
        ans *= i
    return ans

def main():
    for i in range(20):
        print('{}! = {}'.format(i, factorial(i)))

if __name__ == '__main__':
    main()
    