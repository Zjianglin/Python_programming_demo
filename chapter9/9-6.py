'''
9–6. 文件比较. 写一个比较两个文本文件的程序. 如果不同, 给出第一个不同处的行号和
列号.
'''

def diff_files(file1, file2):
    with open(file1, encoding='utf-8') as f1:
        with open(file2, encoding='utf-8') as f2:
            length1 = 0
            length2 = 0

            for i, line1 in enumerate(f1):
                try:
                    line2 = next(f2)
                except:
                    pass

                length1 += len(line1)
                length2 += len(line2)

                for j, ch in enumerate(line1):
                    if ch != line2[j]:
                        return (i + 1, j + 1)
            length1 += sum(len(line) for line in f1)
            length2 += sum(len(line) for line in f2)

            if length1 != length2:
                return (i + 2, 1)
            else:
                return (-1, -1)

def main():
    row, col = diff_files('example', 'example2')
    print(row, col)
    if row > 0:
        print('the first different position is row {}, column {}'.format(row, col))
    else:
        print('The two files are same')

if __name__ == '__main__':
    main()
    