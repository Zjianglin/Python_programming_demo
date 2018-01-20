'''
7-9. 翻译
(a) 编写一个字符翻译程序(功能类似于Unix 中的tr 命令)。我们将这个函数叫做tr()，它有
三个字符串做参数: 源字符串、目的字符串、基本字符串，语法定义如下：
def tr(srcstr, dststr, string)
srcstr 的内容是你打算“翻译”的字符集合，dsrstr 是翻译后得到的字符集合，而string 是
你打算进行翻译操作的字符串。举例来说，如果srcstr == 'abc', dststr == 'mno', string ==
'abcdef', 那么tr()的输出将是'mnodef'. 注意这里len(srcstr) == len(dststr).
在这个练习里，你可以使用内建函数chr() 和 ord(), 但它们并不一定是解决这个问题所必不
可少的函数。
(b) 在这个函数里增加一个标志符参数，来处理不区分大小写的翻译问题。
(c)修改你的程序，使它能够处理删除字符的操作。字符串srcstr 中不能够映射到字符串dststr
中字符的多余字符都将被过滤掉。换句话说，这些字符没有映射到dststr 字符串中的任何字符，因
此就从函数返回的字符里被过滤掉了。举例来说：如果 srcstr == 'abcdef', dststr == 'mno',
string == 'abcdefghi', 那么tr()将输出'mnoghi'. 注意这里len(srcstr) >= len(dststr).
'''

def tr_ab(srcstr, dststr, string, C=True):
    '''
    case-sensitive if C is True.
    '''
    strmap = dict(zip(srcstr, dststr))
    print(strmap)
    if not C:
        s = string.lower()
    else:
        s = string
    
    new_str = [strmap.get(ch, ch) for ch in s]
    return ''.join(new_str)

def tr_c(srcstr, dststr, string, C=True):
    '''
    case-sensitive if C is True.
    '''
    strmap = dict(zip(srcstr, dststr))
    if len(srcstr) > len(dststr):
        tmp = {}.fromkeys(srcstr[len(dststr):], None)
        strmap.update(tmp)
    print(strmap)
    if not C:
        s = string.lower()
    else:
        s = string
    
    new_str = []
    for ch in s:
        if ch not in strmap:
            new_str.append(ch)
        elif ch in strmap and strmap[ch]:
            new_str.append(strmap[ch])
        else:
            continue
    return ''.join(new_str)

def main():
    srcstrs = ['abcdef']
    dststrs = ['mno']
    strings = ['AbcDefghi']

    for src in srcstrs:
        for dst in dststrs:
            for s in strings:
                print('{}-->{}==> {}'.format(src, dst, tr_c(src, dst, s, False))) 
    
if __name__ == '__main__':
    main()
    
