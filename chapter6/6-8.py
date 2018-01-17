'''
6-8.列表。给出一个整型值，返回代表该值的英文，比如输入89返回“eight-nine”。附加
题：能够返回符合英文语法规则的形式，比如输入“89”返回“eighty-nine”。本练习中的值
限定在0~1000。
'''

def english_v1(num):
    maps = { 0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
               5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
               10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
               15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen',
               20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty',
               70: 'seventy', 80: 'eighty', 90: 'ninety'
    }
    if num is None:
        raise ValueError('num cannot be None')
    num = str(num)
    if not num.isdigit():
        raise ValueError('num must be a number')
    result = maps[int(num[0]) - 0]
    for i in range(1, len(num)):
        result += '-' + maps[int(num[i]) - 0]
    return result

def english_v2(num):
    maps = { 0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
               5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
               10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
               15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen',
               20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty',
               70: 'seventy', 80: 'eighty', 90: 'ninety'
    }
    if num is None:
        raise ValueError('num cannot be None')
    num = int(num)
    res = ''
    if not ( 0 <= num <= 1000):
        raise ValueError('num must in range: [0, 1000]')
    
    if num == 0:
        return 'zero'
    elif num == 1000:
        return 'one thousand'
    elif num // 100 : #  100 <= num < 1000
        res = str(maps[num // 100]) + ' hundred'
        num %= 100
        if num:
            res += ' and'
    if num > 20:
        res += ' ' + maps[num // 10 * 10] + '-'
        num %= 10
    if num:
        res += maps[num]
    return res


        

def main():
    nums = [0, 1, 10, 15, 56, 89, 100, 456, 1000]
    print('---english_v1---') 
    for n in nums:
        print('{} in english is: {}'.format(n, english_v1(n)))

    print('---english_v2---') 
    for n in nums:
        print('{} in english is: {}'.format(n, english_v2(n)))

if __name__ == '__main__':
    main()