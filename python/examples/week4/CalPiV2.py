#CalPiV2.py
from random import random
from time import perf_counter
darts = 1000 ** 2
hits = 0
start = perf_counter()
for i in range(darts):
    x, y = random(), random()
    dist = pow(x ** 2 + y ** 2, 0.5)
    if dist <= 1:
        hits += 1
print("圆周率值为:{:f}".format(4 * hits / darts))
print("所耗时间为:{}s".format(perf_counter() - start))

