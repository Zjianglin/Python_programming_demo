"""
9–17. 文本处理. 创建一个原始的文本文件编辑器. 你的程序应该是菜单驱动的, 有如下
这些选项:
1) 创建文件(提示输入文件名和任意行的文本输入),
2) 显示文件(把文件的内容显示到屏幕),
3) 编辑文件(提示输入要修改的行, 然后让用户进行修改),
4) 保存文件, 以及
5) 退出.
"""

import os

def create_file():
    while True:
        fname = input('Enter new file name: ')
        if not fname.strip():
            print('** New file name cannot be empty. Enter again.')
        else:
            fname = fname.strip()
            break

    fhandle = open(fname, 'w', encoding='utf-8')
    lineno = 0
    while True:
        lineno += 1
        try:
            line = input('Enter the {}th line content(Ctrl_C to finish):\n>>'\
                    .format(lineno))
            fhandle.write(line + '\n')
        except KeyboardInterrupt as terminal:
            print('Input completion!\n')
            return fhandle

def print_file(fhandle):
    for line in fhandle:
        print(line)
    print()

def main():
    fhandle = None
    while True:
        print("""\n\n\t\t\t ** Menu **
            1 create a file.
            2 print a target file.
            3 edit target file.
            4 save.
            5 exit.
        """)
        op = input('Enter your operation choice: ').strip()
        if op == '1':
            fhandle = create_file()
        elif op == '2':
            fname = input("Enter target file to print: ")
            if fhandle:
                fhandle.close()
            try:
                with open(fname, 'r', encoding='utf-8') as fhandle:
                    print_file(fhandle)
            except FileNotFoundError as err:
                print(err)
                continue
        elif op == '3':
            fname = input("Enter target file to edit: ")
            try:
                with open(fname, 'r', encoding='utf-8') as fin:
                    new_file = fname + '_new'
                    fout = open(new_file, 'w', encoding='utf-8')
                    
                    lineno = int(input("Enter which line to edit: "))
                    data = input('Enter new data of line {}: '.format(lineno))
                    for i, line in enumerate(fin, 1):
                        if i == lineno:
                            fout.write(data + '\n')
                        else:
                            fout.write(line)
                    fout.close()
                os.remove(fname)
                os.rename(new_file, fname)
            except FileNotFoundError as err:
                print(err)
                continue
        elif op == '4':
            if fhandle:
                fhandle.close()
        elif op == '5':
            break
        else:
            continue

if __name__ == '__main__':
    main()
    
