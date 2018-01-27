'''
9–7. 解析文件. Win32 用户: 创建一个用来解析 Windows .ini 文件的程序. POSIX 用户:
创建一个解析 /etc/serves 文件的程序. 其它平台用户: 写一个解析特定结构的系统配置文件的
程序.
'''

from os import path

def parse_ini(fname):
    if path.splitext(fname)[1] != '.ini':
        raise TypeError('input should be .ini')
    ans = dict()
    section = ''
    with open(fname) as fin:
        for line in fin:
            line = line.strip()
            if not line:
                continue
            elif line[0] == ';':
                #comment --> skip
                continue
            elif line[0] == '[':
                # section
                section = line[1:line.find(']')]
                ans[section] = dict()
            else:
                if ';' in line:
                    line = line[:line.find(';')].strip()
                if section:
                    key, value = line.split('=')
                    ans[section][key] = value
                else:
                    raise ValueError('input file is not INI format')
    return ans

def main():
    ans = parse_ini('demo.ini')
    print('sections: ', ans.keys())
    for section in ans:
        print('[{}]'.format(section))
        for key in ans[section]:
            print('  {} = {} '.format(key, ans[section][key]))

if __name__ == '__main__':
    main()
    

