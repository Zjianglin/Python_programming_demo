"""
9–16. 文本处理. 人们输入的文字常常超过屏幕的最大宽度. 编写一个程序, 在一个文本
文件中查找长度大于 80 个字符的文本行. 从最接近 80 个字符的单词断行, 把剩余文件插入到
下一行处.
程序执行完毕后, 应该没有超过 80 个字符的文本行了.
"""

import sys
import os


def main():
    args = sys.argv
    if len(args) != 2:
        print('**Error: A target file should be specified.')
        return -1
    cp = args[1] + '.copy'
    copy = False
    fcopy = open(cp, 'w', encoding='utf-8')
    pre = ''
    with open(args[1], 'r', encoding='utf-8') as fin:
        for eachLine in fin:
            line = ' '.join([pre, eachLine]) if pre else eachLine
            if len(line) <= 80:
                fcopy.write(line)
                if eachLine == '\n' and line != '\n':
                    fcopy.write('\n')
            else:
                while len(line) > 80:
                    copy = True
                    index = line.rfind(' ', 0, 80)
                    fcopy.write('{}\n'.format(line[:index]))
                    line = line[(index + 1):]
                if len(line.strip()):
                    pre = line.strip()

    if pre:
        fcopy.write('{}\n'.format(pre))
    fcopy.close()
    if copy:
        os.remove(args[1])
        os.rename(cp, args[1])
    else:
        os.remove(cp)
                
if __name__ == '__main__':
    main()
    