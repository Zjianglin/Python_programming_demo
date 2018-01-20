'''
7-4. 建立字典。给定两个长度相同的列表，比如说，列表[1, 2, 3,...]和['abc', 'def',
'ghi',...],用这两个列表里的所有数据组成一个字典，像这样：{1:'abc', 2: 'def', 3: 'ghi',...}
'''

def creat_dict(l1, l2):
    return dict(zip(l1, l2))

def main():
    l1 = [i for i in range(10)]
    l2 = [v for v in 'abcdefghik']

    print(creat_dict(l1, l2))

if __name__ == '__main__':
    main()
    