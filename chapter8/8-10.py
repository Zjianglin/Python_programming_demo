'''
8–10. 文本处理. 统计一句话中的元音, 辅音以及单词(以空格分割)的个数. 忽略元音和
辅音的特殊情况, 如 "h", "y", "qu" 等. 附加题: 编写处理这些特殊情况的代码.
'''
'''
暂不处理特殊情况
'''
import string

def counts(sentence):
    vowels = set('aeiou')
    consonants = set(string.ascii_lowercase) - vowels

    sentence = sentence.lower()

    cwords = len([word for word in sentence.split()])
    count_vowel = sum(1 for ch in sentence if ch in vowels)
    count_consonant = sum(1 for ch in sentence if ch in consonants)


    return (count_vowel, count_consonant, cwords)

def main():
    sentence = 'A function which returns an iterator.'
    ans = counts(sentence)
    print(sentence)
    print('vowels: {}, consonants: {}, words: {}'.format(ans[0], ans[1], ans[2]))

if __name__ == '__main__':
    main()
    