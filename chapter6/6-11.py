
'''
6-11.转换。
（a）创建一个从整型到IP地址的转换程序，如下格式；WWW.XXX.YYY.ZZZ。
（b）更新你的程序，使之可以逆转换。
'''

def num2ip(num):
    num = int(num)
    if num < 0 or num >= pow(2, 32):
        raise ValueError('input number is invalid')
    base = 0b11111111
    f = lambda i: '{:}'.format(i)
    ip = []
    for i in range(4):
        ip.insert(0, f(num & base))
        num = num >> 8
    return '.'.join(ip)

def ip2num(ip):
    ip = str(ip)
    ns = [int(i) for i in ip.split(r'.')]
    num = 0
    for i in range(4):
        num = (num << 8) + ns[i]
    return num

def main():
    ips = ['192.168.1.2', '0.184.244.124', '1.98.52.157', 
           '1.238.190.8', '0.52.95.231', '140.82.109.216']
    for ip in ips:
        print('IP: {:15} number: {:15}'.format(ip, ip2num(ip)))
    
    nums = [3232235778, 12121212, 23213213, 32423432, 3432423, 2354212312]
    for num in nums:
        print('IP: {:15} number: {:15}'.format(num2ip(num), num))

if __name__ == '__main__':
    main()