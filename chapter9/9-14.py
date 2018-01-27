'''
9–14. 记录结果. 修改你的计算器程序(练习 5-6)使之接受命令行参数. 例如:
$ calc.py 1 + 2
只输出计算结果. 另外, 把每个表达式和它的结果写入到一个磁盘文件中. 当使用下面的命令
时:$ calc.py print 会把记录的内容显示到屏幕上, 然后重置文件.
'''
import sys

def main():
    args = sys.argv[1:]
    if not len(args):
        print('**No equaltion or print argment')
        return
    if args[0].strip() == 'print':
        with open('cal_base.txt', 'r+', encoding='utf-8') as fin:
            for line in fin:
                print(line)
            fin.truncate(0)
    else:
        equation = ' '.join(args)
        ans = eval(equation.replace('^', '**'))
        with open('cal_base.txt', 'a') as fout:
            fout.write(equation + '\n')
            fout.write('{}\n'.format(ans))

        print(ans)

if __name__ == '__main__':
    main()
    