'''
6-17.方法。实现一个叫myPop()的函数，功能类似于列表的pop()方法，用一个列表作为
输入，移除列表的最新一个元素，并返回它。
'''

def myPop(List):
    if not List:
        raise ValueError('MyPop from empty list')
    return List[:-1]


def main():
    ls = [
        #[],
        [0],
        [0, 1, 2,2 ,3]
    ]
    for l in ls:
        print('myPop({}) is {} '.format(l, myPop(l)))
    
if __name__ == '__main__':
    main()
    