'''
6-15.转换。
（a）给出两个可识别格式的日期，比如MM/DD/YY或者DD/MM/YY格式，计算出两
个日期间的天数。
（b）给出一个人的生日，计算从此人出生到现在的天数，包括所有的闰月。
（c）还是上面的例子，计算出到此人下次过生日还有多少天。
'''
import time

def date2num(ds):
    '''
    format: DD/MM/YYYY
    return the number of days since 1/1/1900
    '''
    months = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    date = [int(i) for i in ds.strip().split('/')]
    is_leap_year = lambda y: (y % 400 == 0) or (y % 4 == 0 and y % 100)
    days =  date[0] + sum(months[:date[1]])
    if is_leap_year(date[2]) and date[1] > 2:
        days += 1
    years = (date[2] - 1900)
    days += (365 * years + years // 4) 
    return days

def days_gap(date1, date2):
    '''
    date1 and date2 are string
    '''
    return abs(date2num(date1) - date2num(date2))

def birthed_days(birthday):
    dnow = time.localtime()
    dn = [dnow.tm_mday, dnow.tm_mon, dnow.tm_year]
    dn = [str(i) for i in dn]
    return days_gap(birthday, '/'.join(dn))

def next_birthday(birthday):
    dnow = time.localtime()
    dn = [dnow.tm_mday, dnow.tm_mon, dnow.tm_year]
    db = [int(i) for i in birthday.strip().split('/')]

    if dn[1] == db[1] and dn[0] < db[0]: #same month, birthday doesn't pass
        return dn[0] - db[0] + 1
    elif dn[1] > db[1] or (dn[1] == db[1] and dn[0] < db[0]): #this year passed
        date2 = '/'.join([str(db[0]), str(db[1]), str(dn[2] + 1)])
    else:
        date2 = '/'.join([str(dn[0]), str(dn[1]), str(dn[2])])
    date1 = '/'.join([str(db[0]), str(db[1]), str(dn[2])])
    return days_gap(date1, date2)
        
def main():
    dates = ['2/1/1900', '16/1/2017', '16/1/2018']
    birthdays = ['6/1/2017', '26/2/2017']

    for d in dates:
        print("days between '{}' and '{}': {}".format(d, '16/1/2018', 
                days_gap(d, '16/1/2018')))
    
    for b in birthdays:
        print("birthday is {}, has been {} days since born, {} to next birthday".format(
            b, birthed_days(b), next_birthday(b)
        ))

if __name__ == '__main__':
    main()
    
