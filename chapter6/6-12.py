'''
6-12.字符串。
（a）创建一个名字为findchr()的函数，函数声明如下。
    def findchr （string, char）
findchr()要在字符串string中查找字符char，找到就返回该值的索引，否则返回-1。
不能用string.*fmd()或者string.*index()函数和方法。
（b）创建另一个叫rfindchr()的函数，查找字符char最后一次出现的位置。它跟findchr()工作类似，不过它是从字符串的最后开始向前查找的。
（c）创建第三个函数，名字叫subchr()，声明如下。
    def subchr（string, origchar, newchar）
subchr()跟findchr()类似，不同的是，如果找到匹配的字符就用新的字符替换原先字符。返回修改后的字符串。
'''

def findchr(string, char):
    if char not in string:
        return -1
    for i in range(len(string)):
        if string[i] == char:
            return i

def rfindchr(string, char):
    if char not in string:
        return -1
    for i in range(len(string) - 1, -1, -1):
        if string[i] == char:
            return i

def subchr(string, origchar, newchar):
    if origchar not in string:
        return string
    for i in range(len(string)):
        if string[i] == origchar:
            return string[:i] + newchar + string[i+1:]

def main():
    strs = ['hello world', 'sdadas', 'world h']
    for s in strs:
        print('"{}".index({}) = {}'.format(s, 'h', findchr(s, 'h')))
        print('"{}".rindex({}) = {}'.format(s, 'h', rfindchr(s, 'h')))
        print('subchr({},{}, {}) = {}'.format(s, 'h', 'H', subchr(s, 'h', 'H')))
    
if __name__ == '__main__':
    main()