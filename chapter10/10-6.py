"""
10–6. 改进的 open(). 为内建的 open() 函数创建一个封装. 使得成功打开文件后, 返
回文件句柄; 若打开失败则返回给调用者 None , 而不是生成一个异常. 这样你打开文件时就不需
要额外的异常处理语句.
"""

def Open(file, mode='r', buffering=-1, encoding=None, \
        errors=None, newline=None, closefd=True, opener=None):
    try:
        fd = open(file, mode, buffering, encoding,
            errors, newline, closefd, opener)
        return fd
    except Exception:
        return None

def main():
    fnames = ['10-4.py', 'README.md', 'test', 'no_exist']
    for f in fnames:
        fd = Open(f, encoding="utf-8")
        if fd:
            for line in fd:
                print(line)
        else:
            print(f, ' no exist')
        print('-' * 20)

if __name__ == '__main__':
    main()
    