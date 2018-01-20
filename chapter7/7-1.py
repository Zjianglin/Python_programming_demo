'''
7–1. 字典方法。哪个字典方法可以用来把两个字典合并到一起？
solution: 
(1). dict.update(d2); 
(2). for k, v in d2.items():
         d1[k] = v
'''

def union_dict(d1, d2):
    print('{:*^12}'.format('BEFORE UNION'))
    print(d1)
    print(d2)

    dc = d1.copy()
    print('solution 1:')
    for k, v in d2.items():
        dc[k] = v
    print(dc)


    dc = d1.copy()
    print('solution 2:')
    dc.update(d2)
    print(dc)

def main():
    d1 = {'a': 1, 'b': 2}
    d2 = {'c': 3, 'd': 4}
    union_dict(d1, d2)

    d1 = {}
    union_dict(d1, d2)
    

if __name__ == '__main__':
    main()
    