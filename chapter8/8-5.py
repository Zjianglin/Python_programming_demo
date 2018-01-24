'''
8–5. 约数. 完成一个名为 getfactors() 的函数. 它接受一个整数作为参数, 返回它所有
约数的列表, 包括 1 和它本身,
'''

def getfactors(num):
    if num <= 1:
        return [0, 0, 1][:num:-1]
    else:
        i = 2
        factors = [1, num]
        while (i ** 2 <= num):
            if num % i == 0:
                factors.append(i)
                if i * i < num:
                    factors.append(num // i)
            i += 1
        return sorted(factors)

def main():
    for i in range(5):
        print('{} = multiply of {}'.format(i, getfactors(i)))
    
    for i in range(6, 100, 10):
        print('{} = multiply of {}'.format(i, getfactors(i)))

if __name__ == '__main__':
    main()
    