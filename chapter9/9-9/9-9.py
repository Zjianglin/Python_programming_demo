'''
9–9. Python 文档字符串. 进入 Python 标准库所在的目录. 检查每个 .py 文件看是否有
__doc__ 字符串, 如果有, 对其格式进行适当的整理归类. 你的程序执行完毕后, 应该会生成一个
漂亮的清单. 里边列出哪些模块有文档字符串, 以及文档字符串的内容. 清单最后附上那些没有文
档字符串模块的名字.
附加题: 提取标准库中各模块内全部类(class)和函数的文档.
'''
import os
from importlib import import_module

def listdoc_1(lib_dir):
    """Use built-in funtion to inspect modules"""
    libs = os.listdir(lib_dir)
    for lib in libs:
        lib = os.path.splitext(lib)
        if lib[-1] != '.py':
            continue
        else:
            try:
                obj = import_module(lib[0])
                yield (lib[0], obj.__doc__)
            except:
                continue


def listdoc_2(lib_dir):
    """manually inspect a module"""
    libs = os.listdir(lib_dir)
    fwith_doc = open('module&doc.txt', 'w+', encoding='utf-8')
    fno_doc = open('module_without_doc.txt', 'w+', encoding='utf-8')

    for lib in libs:
        if os.path.splitext(lib)[-1] != '.py':
            continue
        else:
            with open(os.path.join(lib_dir, lib), encoding='utf-8') as fin:
                doc = ""
                for line in fin:
                    if line[0] == '#':
                        continue
                    elif not doc and not line.strip():
                        continue
                    elif  not (doc or (line.startswith('"""') or line.startswith('r"""') \
                                    or line.startswith("'''") or line.startswith("r'''"))):
                        break
                    else:
                        doc += line
                        if line.endswith('"""\n') or line.endswith("'''\n"):
                            break
                if doc:
                    fwith_doc.write(lib[:-3] + '\n')
                    fwith_doc.write(doc + '\n')
                    fwith_doc.write('==='*30 + '\n')
                else:
                    fno_doc.write(lib[:-3]+ '\n')
                    fno_doc.write('==='*20 + '\n')


def list_CF(lib):
    """extract the doc of classes and functions of a module"""
    lib_name = os.path.splitext(os.path.split(lib)[-1])[0]
    fout = open('{}_doc.txt'.format(lib_name), 'w', encoding='utf-8')
    with open(lib, encoding='utf-8') as fin:
        Type = ""
        name = ""
        doc = ""
        for line in fin:
            if line.startswith("def"):
                Type = "<class 'function'>"
                name = line[4:line.find('(')]
            elif line.startswith("class"):
                Type = "<class 'class'>"
                name = line[6:line.find(':')]
            else:
                line_c = line.strip()
                if not line_c:
                    pass 
                elif not name:
                    #not after a class nor a funtion
                    pass
                elif not (doc or line_c.startswith('"""') or line_c.startswith('r"""') or \
                    line_c.startswith("'''")  or line_c.startswith("r'''")):
                    #no doc
                    fout.write('{}.{}: {}\n'.format(lib_name, name, Type))
                    fout.write("No docstring!")
                    fout.write('\n' + '===' * 10 + '\n')
                    name = ""
                    doc = ""
                else:
                    doc += line
                    if line.endswith('"""\n') or line.endswith("'''\n"):
                        fout.write('{}.{}: {}\n'.format(lib_name, name, Type))
                        fout.write(doc)
                        fout.write('\n' + '===' * 10 + '\n')
                        doc = ""
                        name = ""
    fout.close()

def main():
    lib_dir = 'D:\\Anaconda3\\Lib'
    
    # for lib, doc in listdoc_1(lib_dir):
    #     print('**{}**'.format(lib))
    
    #listdoc_2(lib_dir)
    lib = lib_dir + "\\" + 'types.py'
    print(lib)
    list_CF(lib)
    
if __name__ == '__main__':
    main()
    