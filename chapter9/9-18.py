"""
9–18. 搜索文件. 提示输入一个字节值(0 - 255)和一个文件名. 显示该字符在文件中出现
的次数.
"""

def main():
    value = int(input("Enter a byte value to search(0 - 255): "))
    fname = input("Enter target file: ")

    ch = chr(value)
    with open(fname, encoding="utf-8") as fin:
        count = sum(line.count(ch) for line in fin)
    print("{} occurs {} times in file <{}>".format(ch, count, fname))

if __name__ == '__main__':
    main()
    