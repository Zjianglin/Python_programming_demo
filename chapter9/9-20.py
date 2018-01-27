"""
9–20. 压缩文件. 写一小段代码, 压缩/解压缩 gzip 或 bzip 格式的文件. 可以使用命令
行下的 gzip 或 bzip2 以及 GUI 程序 PowerArchiver , StuffIt , 或 WinZip 来确认你的 Python
支持这两个库.
"""
import gzip

def compress(zipfile, fname):
    dst = gzip.open(zipfile, 'wb')
    with open(fname, 'rb') as fin:
        dst.writelines(fin)
    dst.close()

def decompress(zipfile, fname):
    fin = gzip.open(zipfile, 'rb')
    with open(fname, 'wb') as fout:
        fout.writelines(fin)
    fin.close()

def main():
    compress('test.zip', 'example2')
    decompress('test.zip', 'example3')


if __name__ == '__main__':
    main()
    