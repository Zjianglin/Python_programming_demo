'''
6-9.转换。为练习5-13写一个姊妹函数，接受分钟数，返回小时数和分钟数。总时间不
变，并且要求小时数尽可能大。
'''

def transform2hour(minutes):
    return divmod(minutes, 60)

def main():
    ms = [0, 10, 59, 60, 100, 233]
    for m in ms:
        t = transform2hour(m)
        print('{} minutes is {} hour(s) and {} minute(s)'.format(m, t[0], t[1]))

if __name__ == '__main__':
    main()