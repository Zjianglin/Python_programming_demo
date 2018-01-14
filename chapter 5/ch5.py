# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#5.4
def is_leap_year(year):
    return year % 400 == 0 or year % 4 == 0 and year % 100

#5-12
    
#5-14 最大公约数和最小公倍数。请计算两个整型的最大公约数和最小公倍数
def gcd_(a, b):
    if b:
        return gcd_(b, a%b)
    else:
        return a

def gcd(a, b):#最小公倍数
    if a > b :
        return gcd_(a, b)
    else:
        return gcd_(b, a)


def lcm(a, b): #公式法：最小公倍数 = 两数乘积/最大公约数
    return int(a * b / gcd(a, b))


        


def main():
    years = [1992, 1996, 2000, 2004, 2008, 1900, 1967]
    for year in years:
        if is_leap_year(year):
            print(year, 'is a leap year')
        else:
            print(year, 'is not a leap year')
    
    print('-'*20)
    for t in [(1, 2), (2, 4), (3, 5), (222, 18)]:
        print('lcm({t1}, {t2})={l}, gcd({t1}, {t2})={g}'.format(
              t1=t[0], t2=t[1], l=lcm(t[1], t[0]), g=gcd(t[1], t[0])))
            
if __name__ == '__main__':
    main()