#AutoTraceDraw.py 
import turtle as tt 
tt.title('自动轨迹绘制')
tt.setup(800, 600, 0, 0)
tt.pencolor('red')
tt.pensize(5)
#读取数据
datals = []
f = open('data.txt')
for line in f:
    line = line.strip()
    line = line.replace(' ', '')
    datals.append(list(map(eval, line.split(','))))
    #datals.append(map(eval, line.split(',')))
    '''之所以需要list来进行列表处理，是因为从python3.x开始map函数返回的是一个迭代器'''
f.close() 
for i in range(len(datals)):
    tt.pencolor(datals[i][3], datals[i][4], datals[i][5])
    tt.fd(datals[i][0])
    if datals[i][1]:
        tt.right(datals[i][2])
    else:
        tt.left(datals[i][2])
tt.done()
