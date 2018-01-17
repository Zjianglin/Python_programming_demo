
# -*- coding:utf-8 -*-

'''
6-17.方法。实现一个叫myPop()的函数，功能类似于列表的pop()方法，用一个列表作为
输入，移除列表的最新一个元素，并返回它。
'''


fn = ['AAA', 'BBB', 'CCC']
ln = ['aa', 'bb', 'cc']

print(zip(fn, ln))

'''
zip(iter1, iter2)
Result:
 1. python2中返回一个元组列表，第i个元组是(iter1[i], iter2[i]), 返回列表长度等于较短的参数列表长度
 2. python3中返回一个zip对象(也是一个生成器)，生成的第i个元素也是一个元组，内容同python2
'''