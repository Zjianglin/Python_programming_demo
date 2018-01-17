'''
string模块中并没有实现一个atoc()函数，那么你来实现一个atoc()，接受单个字符串
做参数输入，一个表示复数的字符串，例如‘-1. 23e+4-5.67j’，返回相应的复数对
象。你不能用eval()函数，但可以使用complex()函数，而且你只能在如下的限制之
下使用：complex():complex（real，imag）的real和imag都必须是浮点值。
'''

import re

def atoc(s):
    s = str(s).lower().replace(' ', '')
    if 'j' in s and  '' not in s.split('j'):
        #the imag part is before the real part
        nums = s.split('j')
        return complex(float(nums[1]), float(nums[0]))
    else:
        cp = re.compile(r'''((?P<real>^[+-]?\d+([.]\d*[eE][+-]?\d+)?))?\s*((?P<imag>[+-]\d+([.]\d*([eE][+-]\d+)?)?)[jJ])?''')
        res = cp.match(s).groupdict()
        if not res['real']:
            res['real'] = 0
        if not res['imag']:
            res['imag'] = 0
        return complex(float(res.get('real')), float(res.get('imag')))

def main():
    strs = ['-1.23e+4-5.67j', '-2j', '-20.e1', '-2.5j']
    for s in strs:
        print("complex '{}' is : {}".format(s, atoc(s)))
    
    print(atoc(input('input complex:')))

if __name__ == '__main__':
    main()