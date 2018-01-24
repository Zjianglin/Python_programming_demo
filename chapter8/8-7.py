'''
8–7. 全数. 完全数被定义为这样的数字: 它的约数(不包括它自己)之和为它本身. 例如: 6的约数是 1, 2, 3,
因为 1 + 2 + 3 = 6 , 所以 6 被认为是一个完全数. 编写一个名为 isperfect()的函数, 
它接受一个整数作为参数, 如果这个数字是完全数, 返回 1 ; 否则返回 0 .
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

def isperfect(num):
    factors = getfactors(num)
    return sum(factors[:-1]) == num

def main():
    for i in range(10000):
        if isperfect(i):
            print(i, 'is perfect')

if __name__ == '__main__':
    main()
    