'''
9–8. 模块研究. 提取模块的属性资料. 提示用户输入一个模块名(或者从命令行接受输入).
然后使用 dir() 和其它内建函数提取模块的属性, 显示它们的名字, 类型, 值.
'''
'''
reference: http://www.xmanblog.net/2015/04/29/%E3%80%8Apython%E6%A0%B8%E5%BF%83%E7%BC%96%E7%A8%8B%E3%80%8B%E7%AC%AC%E4%B9%9D%E7%AB%A0%E7%BB%83%E4%B9%A0%E8%A7%A3%E6%9E%90/#8
'''


def check_module(name):
    obj = __import__(name)

    attrs = dir(obj)
    for item in attrs:
        print('name: ', item)
        print('type: ', type(getattr(obj, item)))
        print('value: ', getattr(obj, item))
        print()


def main():
    module = input('Enter the module to study: ')
    check_module(module)


if __name__ == '__main__':
    main()
