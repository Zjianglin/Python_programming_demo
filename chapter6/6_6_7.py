#6.6 创建一个string.strip()的替代函数：接受一个字符串，去掉它前面和后面的空格
def Strip(mystr):
    import re 
    start = re.compile(r'^\s+')
    end = re.compile(r'\s+$')
    mystr = str(mystr)
    find = start.search(mystr)
    if find:
        mystr = mystr[find.end():]
    find = end.search(mystr)
    if find:
        mystr = mystr[:find.start()]
    return mystr

#6.7 
def buggy():
    #该段代码想做的事是：找到所有小于等于输入数字且不能整除输入数字的数字
    num_str = input('Enter a number: ')
    num_num = int(num_str)
    fac_list = list(range(1, num_num+1))
    print("BEFORE:", fac_list)
    
    i = 0
    while i < len(fac_list):
        
        #删去能整除输入整数的列表值
        if num_num % fac_list[i] == 0:
            del fac_list[i]
        else: #add
            i = i + 1
    print('AFTER:', fac_list) #原意应是输出处理后的列表。原代码中fac_list用单引号括起来不能达到题意



def main():
    '''
    strs = ['hello', '  hello world', 'hello   ', ' hello world ']
    for s in strs:
        print("ori: '{}', stripped:'{}'".format(s, Strip(s)))
    '''
    buggy()

if __name__ == '__main__':
    main()