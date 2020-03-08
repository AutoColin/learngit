import time
scale = 50
print("执行开始".center(scale,'-'))
start = time.perf_counter()
for i in range(scale + 1):
    a = '*' * i
    b = '.' * (scale - i)
    c = i * 2
    dur = time.perf_counter() - start 
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur),end = "")
    time.sleep(0.1)
print("\n"+"执行开始".center(scale,'-'))
