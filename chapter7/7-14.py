'''
7–14. 用户验证。修改前面的练习，要求用户输入A | B 和A & B 的结果，并告诉用户他(或
她)的答案是否正确，而不是将A | B 和A & B 的结果直接显示出来。如果用户回答错误，允许他(或
她)修改解决方案，然后重新验证用户输入的答案。如果用户三次提交的答案均不正确，程序将显示
正确结果。
附加题：运用你关于集合的知识，创建某个集合的潜在子集，并询问用户此潜在子集是否真是
该集合的子集，要求和主程序一样有显示更正和答案的功能。
'''
import random

def test(data, info='A | B'):
    for i in range(3, 0, -1):
        guess = input('Enter {} (data alone): '.format(info)).strip()
        guess = {int(i) for i in guess.split()}
        if guess == data:
            print('Congratulations! You\'re right!')
            return None
        else:
            print('Wrong. You can try another {} times!'.format(i - 1))
            continue
    print(info, 'is ', data)

def main():
    while True:
        A = {random.randrange(0, 10) for i in range(random.randint(1, 10))}
        B = {random.randrange(0, 10) for i in range(random.randint(1, 10))}
        union = A | B
        intersection = A & B
        print('***' * 5)
        print('A is ', A)
        print('B is ', B)
        test(union, 'A | B')
        test(intersection, 'A & B')

if __name__ == '__main__':
    main()
    
