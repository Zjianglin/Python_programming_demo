'''
9–15. 复制文件. 提示输入两个文件名(或者使用命令行参数). 把第一个文件的内容复制
到第二个文件中去.
'''
import sys

def copy2(filel, file2):
    try:
        f1 = open(filel, 'r', encoding='utf-8')
        with open(file2, 'w', encoding='utf-8') as fout:
            for line in f1:
                fout.write(line)
        f1.close()
    except Exception as err:
        print(err)

def main():
    args = sys.argv
    if len(args) != 3:
        print('Error: the src and dst file must be specified!')
        return -1
    else:
        print('Copy content of {} to {}...'.format(args[1], args[2]))
        copy2(args[1], args[2])

if __name__ == '__main__':
    main()
    