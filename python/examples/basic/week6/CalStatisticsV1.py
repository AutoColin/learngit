#CalStatisticsV1.py
def getnum():       #获取用户不定长输入
    nums = []
    iNumStr = input("请输入数字(回车退出)")
    while iNumStr != "":
        nums.append(eval(iNumStr))
        iNumStr = input("请输入数字(回车退出)")
    return nums

def mean(numbers):  #计算平均值 
    s = 0.0
    for num in numbers:
        s += num
    return s / len(numbers)

def dev(numbers, mean):     #计算方差
    sdev = 0.0
    for num in numbers:
        sdev = sdev + (num - mean)**2
    return pow(sdev / (len(numbers) - 1), 0.5)

def median(numbers):               #计算中位数
    numbers.sort()      #原视频使用的sorted(numbers),它是返回一个新的排序后的列表，但是原列表是不变的，使用错误
    size = len(numbers)
    if size % 2 == 0:
        med = (numbers[size // 2 - 1] + numbers[size // 2]) / 2
    else:
        med = numbers[size // 2]
    return med

n = getnum()
m = mean(n)
print("平均值:{},方差:{:.2},中位数:{}.".format(m, dev(n, m), median(n)))
