#PythonDraw.pr
import turtle as tt
tt.setup(650, 350, 200, 200)
tt.penup()
tt.fd(-250)
tt.pendown()
tt.pensize(25)
tt.pencolor("purple")
tt.seth(-40)
for i in range(4):
    tt.circle(40, 80)
    tt.circle(-40, 80)
tt.circle(40, 80/2)
tt.fd(40)
tt.circle(16, 180)
tt.fd(40 * 2 / 3)
tt.done()
