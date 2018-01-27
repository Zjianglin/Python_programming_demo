# Chapter 9 Files and Input/Output

## 9.1 文件对象

文件是连续的字节序列。内建函数`open()`返回一个文件对象，对该文件的后续读写等操作均要用到它，还有其他大量的函数也会返回文件对象或类文件(file-like)对象，进行这种抽象处理的原因是为输入/输出结构提供通用的接口。

1. 文件的打开： 内建函数`open()`. 打开模式有读`r(default)`, 写`w`, 读写`r+`, 读写`w+`、添加`a`等多种。写模式打开文件时，若文件不存在则创建文件，否则覆写原来的文件内容。`open()`成功打开文件后会返回一个文件对象，否则引发一个异常错误，具体参考[open()](https://docs.python.org/3.0/library/functions.html#open)

> python2中有内建函数`file()`,功能与`open()`相同，可任意替换。

2. 文件的操作方法： **输入、输出、文件内移动、杂项操作**

* 文件的读入主要有：`read()`,`readline()`, `readlines()`，遍历文件的每一行推荐用for遍历：```for eachLine in file_obj```。使用输入方法如`read()`或`readline()`从文件中读入行时，python并不会自动删除**行结束符**。
```python
with open(path) as fin:
    print(fin.readlines())
    
['this is line 0 \n', 'this is line 1 \n', 'this is line 2 \n', 'this is line 3 \n', 'this is line 4 \n']
```
* 文件的输出: `write()`, `writelines()`，后者相当于多次调用前者。输出方法也不会自动加入行结束符，需要用户在写文件时自己处理。

* 文件内移动: `seek(cookie, whence=0, /)`,改变文件内文件指针的位置。`cookie`字节代表相对于某个位置的偏移量，默认位置whence=0表示从文件头开始算起，1表示从当前位置开始算起，2表示从文件末尾算起。

* 杂项操作：`trunctate()`,`tell()`等。

3. 标准文件：标准输入(一般是键盘)、标准输出(显示器的缓存输出)、标准错误(屏幕的非缓存输出)；这三个文件只要程序一运行就被预先打开。python中通过`sys`模块来访问这三个文件句柄，分别是：`sys.stdin`, `sys.stdout`, `sys.stderr`。

4. 命令行参数: `sys.argv`获得程序的命令行参数列表，`len(sys.argv)`获得参数数量（即C语言的argc）。

5. 文件系统: `os`, `os.path`模块提供了访问计算机文件系统的大部分方法,以及管理进程和进程运行环境的方法。
