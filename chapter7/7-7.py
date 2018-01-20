'''
7-7. 颠倒字典中的键和值。用一个字典做输入，输出另一个字典，用前者的键做值，前者的
值做键。
'''

def exchange_kv(d):
    d1 = dict(d)
    d2 = dict()
    for k in d1.keys():
        d2[d1[k]] = k
    return d2

def main():
    d1 = {'a': 1, 'b': 2, 'c': 3}
    print(d1)
    print('exchange key and value =>')
    print(exchange_kv(d1))

if __name__ == '__main__':
    main()
    