'''
8–12. (整数)位操作. 编写一个程序, 用户给出起始和结束数字后给出一个下面这样的表格,
分别显示出两个数字间所有整数的十进制, 二进制, 八进制和十六进制表示. 如果字符是可打印的
ASCII 字符, 也要把它打印出来, 如果没有一个是可打印字符, 就省略掉 ASCII 那一栏的表头.
'''
'''
printable ASCII characters: 0x20 <= ord(ch) <= 0x7e
'''


def main():
    start = int(input('Enter begin value: '))
    end = int(input('Enter end value: '))
    has_printable = 0x20 <= start <= 0x7e or 0x20 <= end <= 0x7e
    
    if start > end:
        print('start should less or equal than end')
        return -1
    
    if has_printable:
        print('{:5}\t{:10}\t{:6}\t{:6}\t{:5}'.format('DEC', 'BIN', 'OCT', 'HEX', 'ASCII'))
    else:
        print('{:5}\t{:10}\t{:6}\t{:6}\t'.format('DEC', 'BIN', 'OCT', 'HEX'))
    print('-' * 50)

    for i in range(start, end + 1):
        bn = bin(i)[2:]
        on = oct(i)[2:]
        hn = hex(i)[2:]
        if has_printable and (0x20 <= i <= 0x7e):
            print('{:5}\t{:0>9}\t{:6}\t{:6}\t{:5}'.format(i, bn, on, hn, chr(i)))
        else:
            print('{:5}\t{:0>8}\t{:6}\t{:6}'.format(i, bn, on, hn))

if __name__ == '__main__':
    main()
    