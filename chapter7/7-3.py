# -*- coding: utf-8 -*-
'''
7-3. 字典和列表的方法。
(a) 创建一个字典，并把这个字典中的键按照字母顺序显示出来。
(b) 现在根据已按照字母顺序排序好的键，显示出这个字典中的键和值。
(c)同(b),但这次是根据已按照字母顺序排序好的字典的值，显示出这个字典中的键和值。(注
意：对字典和哈希表来说，这样做一般没有什么实际意义，因为大多数访问和排序(如果需要)都是
基于字典的键，这里只把它作为一个练习。)
'''

def main():
    d = {'a': 1, 'e': 5, 'd': 3, 'c': 4, 'f': 2}
    print(d)
    #(a)
    keys = sorted(d.keys())
    print(keys)

    #(b)
    for k in keys:
        print(k, d[k])

    print('***c***')
    keys = sorted(d, key=lambda k: d[k])
    for k in keys:
        print(k, d[k])


if __name__ == '__main__':
    main()
    