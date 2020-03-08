#KockDrawV2.py
import turtle as tt
def koch(size, n):
    if n == 0:
        tt.fd(size)
    else:
        for angle in [0, 60, -120, 60]:
            tt.left(angle)
            koch(size / 3, n - 1)
def main():
    length, level, sp = eval(input())
    tt.setup(600, 600) 
    tt.speed(sp)
    tt.penup()
    tt.goto(-200, 200)
    tt.pendown()
    tt.pensize(2)
    koch(length, level)
    tt.right(120)
    koch(length, level)
    tt.right(120)
    koch(length, level)
    tt.hideturtle()
    tt.done()
main()
