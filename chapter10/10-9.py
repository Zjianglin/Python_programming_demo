"""
10–9. 改进的 math.sqrt(). math 模块包含大量用于处理数值相关运算的函数和常量. 不
幸的是, 它不能识别复数, 所以我们创建了 cmath 模块来支持复数相关运算. 请创建一个
safe_sqrt() 函数, 它封装 math.sqrt() 并能处理负值, 返回一个对应的复数.
"""
from math import sqrt

def safe_sqrt(num):
    if num < 0:
        return complex(0, sqrt(abs(num)))
    else:
        return sqrt(num)

def main():
    for i in [1, -1, 4, -4, 8, -8]:
        print('safe_sqrt({}) = {}'.format(i, safe_sqrt(i)))

if __name__ == '__main__':
    main()
    