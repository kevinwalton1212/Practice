import random as Ra

def Roll_dice():      ##摇骰子，得到三个骰子的点数
    print('===========Roll the dice!===========')
    points = []
    for x in range(1,4):
        points.append(Ra.randrange(1, 7))  #append是没有返回值的，直接对列表进行增加元素
    return points

def Rool_Result(total):     ##定义摇骰子结果大还是小
    is_small = (3 <= total <= 10)
    is_big =  (11 <= total <= 18)
    if is_small:
        return 'small'
    elif is_big:
        return 'big'
    else:
        return 'Error'

def start_game(): ##主函数，开始游戏，在游戏过程中记录玩家的钱金额，大于0才可以开始玩，赔率为1:1
    money = int(input('Input your money:'))
    choice = ['small', 'big']
    while money>0:
        print('<<<<<<<<<<<<<<<<<<<<<<< Game Starts! >>>>>>>>>>>>>>>>>>>>>>>>>>')
        guess = input('Guesee small or big:')
        if guess in choice:
            money_bet = int(input('How much you wanna bet? -- '))
            points = Roll_dice()
            total = sum(points)
            Re = Rool_Result(total)
            if guess == Re:
                print('The result is {}. You win!'.format(points))
                money = money + money_bet
                print('You gained {}, You have {} now!'.format(money_bet,money))
            else:
                print('The result is {}. You loose!'.format(points))
                money = money - money_bet
                print('You lost {}, You have {} now!'.format(money_bet,money))
        else:
            print('The invalid iput!')
    else:
        print('You don\'t have enough money!')
    print('<<<<<<<<<<<<<<<<<<<<<<<< Game Over! >>>>>>>>>>>>>>>>>>>>>>>>>>>')

start_game()
