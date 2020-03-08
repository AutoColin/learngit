#MatchAnalysis.py 
from random import uniform 
def printIntro():
    print('本程序模拟两个选手A和B的某竞技比赛结果')
    print('程序运行需要输入A和B的能力值(以0至1之间的小数表示)')

def getInputs():
    a = eval(input('请输入选手A的能力值(0-1):'))
    b = eval(input('请输入选手B的能力值(0-1):'))
    n = eval(input('模拟比赛场次:'))
    return a, b, n

def simNGames(n, probA, probB):
    winsA, winsB = 0, 0
    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB)
        if scoreA > scoreB:
            winsA += 1
        else:
            winsB += 1
    return winsA, winsB

def simOneGame(probA, probB):
    scoreA, scoreB = 0, 0
    if uniform(0, probA) > uniform(0, probB):
        serving = 'A'
    else:
        serving = 'B' 
    #serving = 'A'
    while not gameOver(scoreA, scoreB):
        if serving == 'A':
            if uniform(0, probA) * probB * 100 < probA:
                scoreA += 1
            else:
                serving = 'B'
        else:
            if uniform(0, probB) * probA * 100 < probB:
                scoreB += 1
            else:
                serving = 'A'
    return scoreA, scoreB

def gameOver(a, b):
    return a==15 or b==15

def printSummary(winsA, winsB):
    n = winsA + winsB 
    print('比赛模拟完毕，共模拟{}场比赛'.format(n))
    print('选手A共获胜{}场,占比{:0.1%}'.format(winsA, winsA / n))
    print('选手B共获胜{}场,占比{:0.1%}'.format(winsB, winsB / n))

def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB = simNGames(n, probA, probB)
    printSummary(winsA, winsB)
main()
