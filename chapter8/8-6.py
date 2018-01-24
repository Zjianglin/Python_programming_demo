'''
8-6 素因子分解. 以刚才练习中的 isprime() 和 getfactors() 函数为基础编写一个函
数, 它接受一个整数作为参数, 返回该整数所有素数因子的列表. 这个过程叫做求素因子分解, 它
输出的所有因子之积应该是原来的数字. 注意列表里可能有重复的元素. 例如输入 20 , 返回结果
应该是 [2, 2, 5] .
'''

def isprime(num):
    i = 2;
    while i * i <= num:
        if num % i == 0:
            return False
        i += 2 if i > 2 else 1
    return (num > 1)

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

def pf(num):
    '''prime factorization'''
    if isprime(num):
        raise ValueError('Input is a prime')
    
    factors = getfactors(num)[1:-1]
    result = []
    index = 0
    while num > 1:
        if isprime(factors[index]) and num % factors[index] == 0:
            result.append(factors[index])
            num //= factors[index]
        else:
            index += 1
    return result

def main():
    nums = [4, 6, 8, 12, 15, 20, 45, 100]
    for num in nums:
        print(num, 'prime factorization: ', pf(num))

if __name__ == '__main__':
    main()
    
