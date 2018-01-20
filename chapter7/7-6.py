'''
7-6. 列表和字典。创建一个简单的股票证券投资数据系统。其中应至少包含四项数据：股市
行情显示器符号，所持有的股票，购买价格及当前价位 - 你可以随意添加其他数据项，比如收益率，
52 周最高指数、最低指数，等等。
用户每次输入各列的数据构成一个输出行。每行数据构成一个列表。还有一个总列表，包括了
所有行的数据。数据输入完毕后，提示用户选择一列数据项进行排序。把该数据项抽取出来作为字
典的键，字典的值就是该键对应行的值的列表。提醒读者：被选择用来排序的数据项必须是非重复
的键，否则就会丢失数据，因为字典不允许一个键有多个值。
你还可以选择其他计算输出，比如，盈亏比率，目前证券资产价值等。
'''

def main():
    records = []

    print('*' * 10)
    print('Input id, stock, purchase price and current price(whitspace to separate)')
    print('F to finish')
    print('eg: >>> 001001 SE1 66 56.3')
   
    while True: 
        #input data
        line = input('>>>').split()
        if line[0] == 'F':
            break
        records.append(line)

    print('Select a column to be key(the selected column must be unique):')
    while True:
        index = int(input('')) - 1
        if index < 0 or index > 3:
            print('index exceed the column numbers')
            continue
        break
    d = dict({records[i][index]: records[i] for i in range(len(records))})

    print(d)
    for k in sorted(d.keys()):
        print(k, d[k])

if __name__ == '__main__':
    main()
    
