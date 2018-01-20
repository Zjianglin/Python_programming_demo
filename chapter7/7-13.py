'''
7–13. 随机数。修改练习5-17 的代码：使用random 模块中的randint()或randrange()方
法生成一个随机数集合：从0 到9(包括9)中随机选择，生成1 到10 个随机数。这些数字组成集合
A(A 可以是可变集合，也可以不是)。同理，按此方法生成集合B。每次新生成集合A 和B 后，显示
结果 A | B 和 A & B
'''

import random

def main():
    for loop in range(5):
        A = set([random.randrange(0, 10) for i in range(random.randint(1, 10))])
        B = set([random.randrange(0, 10) for i in range(random.randint(1, 10))])
        print('A = ', A)
        print('B = ', B)
        print('A | B = ', A | B)
        print('A & B = ', A & B)

if __name__ == '__main__':
    main()
    