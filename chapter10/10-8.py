"""
10–8. 改进的 raw_input() . 本章的开头, 我们给出了一个"安全"的 float() 函数,
它建立在内建函数 float() 上, 可以检测并处理 float() 可能会引发的两种不同异常. 同样,
raw_input() 函数也可能会生成两种异常, EOFError (文件末尾 EOF, 在 Unix 下是由于按下了
Ctrl+D 在 Dos 下是因为 Ctrl+Z) 或是 KeyboardInterrupt ( 取消输入, 一般是由于按下了
Ctrl+C). 请创建一个封装函数 safe_input() , 在发生异常时返回 None .
"""

#python3 中, raw_input --> input
def safe_input(promote=''):
    try:
        return input(promote)
    except (EOFError, KeyboardInterrupt) as err:
        return None

def main():
    for i in range(5):
        get = safe_input('>>>')
        if get:
            print('Your input: ', get)
        else:
            print('Input Error')

if __name__ == '__main__':
    main()
    