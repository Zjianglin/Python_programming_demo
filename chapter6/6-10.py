'''
6-10.字符串。写一个函数，返回一个跟输入字符串相似的字符串，要求字符串的大小写
反转。比如，输入“Mr.Ed”，应该返回“mR.eD”作为输出。
'''

def similar(myStr):
    if not myStr:
        return myStr
    tf = lambda ch: ch.upper() if ch.islower() else ch.lower()

    chs = [tf(ch) for ch in list(myStr)]
    return ''.join(chs)


def main():
    strs = ['Mr.Ed', 'hello World', ' Hello WORLD', 'py2PY3']
    for s in strs:
        print('BEFORE: {:12}, AFTER: {:12}'.format(s, similar(s)))
    
if __name__ == '__main__':
    main()
