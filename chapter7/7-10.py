'''
7–10. 加密。
(a) 用上一个练习的思路编写一个"rot13"翻译器。"rot13"是一个古老而又简单的加密方法，
它把字母表中的每个字母用其后的第13 个字母来代替。字母表中前半部分字母将被映射到后半部分，
而后半部分字母将被映射到前半部分，大小写保持不变。举例来说，'a'将被替换为'n','X'将被替
换为'K'; 数字和符号不进行翻译。
(b)在你的解决方案的基础上加一个应用程序，让它提示用户输入准备加密的字符串(这个算法
同时也可以对加密后的字符串进行解密)，如下所示:
'''

def rot13(text):
    map1 = {i: chr(ord('a') + i) for i in range(26)}
    map2 = {i: chr(ord('A') + i) for i in range(26)}

    ch_array = list(text)
    for i, ch in enumerate(ch_array):
        if ch.isalpha():
            if ch.islower():
                ch_array[i] = map1[(ord(ch)-ord('a') + 13) % 26]
            else:
                ch_array[i] = map2[(ord(ch)-ord('A') + 13) % 26]

    return ''.join(ch_array)

def main():
    
    while True:
        string = input('Enter string to rot13:')
        print('Your string to en/decrypt was: [{}]'.format(string))

        print('The rot13 string is: [{}]'.format(rot13(string)))

if __name__ == '__main__':
    main()
    