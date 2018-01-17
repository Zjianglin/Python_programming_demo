'''
6-14.随机数。设计一个“石头、剪子、布”游戏，有时又叫“Rochambeau”，你小时候可能
玩过，下面是规则。你和你的对手，在同一时间做出特定的手势，必须是下面一种：石
头、剪子、布。胜利者从下面的规则中产生，这个规则本身是个悖论。
（a）布包石头。
（b）石头砸剪子。
（c）剪子剪破布。在你的计算机版本中，用户输入她/他的选项，计算机找一个随
机选项，然后由你的程序来决定一个胜利者或者平手。注意：最好的算法是尽量少
的使用if语句。
'''
import random

def Rochambeau():
    '''
    r=rock, s=scissors, c=cloth
    r>s, s>c, c>r
    '''
    rules = {
        ('r', 's'): 1, ('s', 'r'): -1,
        ('s', 'c'): 1, ('c', 's'): -1,
        ('c', 'r'): 1, ('r', 'c'): -1,
        ('r', 'r'): 0, ('s', 's'): 0, ('c', 'c'): 0
    }
    print('{:*^15}'.format('Rochabeau'))
    promat = 'Enter your choice(r="rock", s="scissors", c="cloth", q=quit):'
    legals = ('r', 's', 'c')
    while True:
        user = input(promat).lower()
        if user == 'q':
            break
        if user not in legals:
            print('Your input is illegal')
            continue
        machine = random.choice(legals)
        ans = rules[(user, machine)]
        if  ans > 0:
            print('Congratulations! You are Winner')
        elif ans < 0:
            print('Draw! play again')
        else:
            print('Whoops! Machine is Winner')
        
    print('ByeBye')

if __name__ == '__main__':
    Rochambeau()
    