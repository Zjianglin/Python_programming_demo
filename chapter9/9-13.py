'''
9–13. 命令行参数
a) 什么是命令行参数, 它们有什么用?
b) 写一个程序, 打印出所有的命令行参数.
'''

'''
Solution: 命令行参数是调用某个程序时除程序名以外的其他参数。
'''

import sys

def main():
    print(sys.argv)

if __name__ == '__main__':
    main()
    