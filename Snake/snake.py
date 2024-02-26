# 引用数据库
from turtle import *
from random import randrange
from time import *

# 定义变量
snake = [[0, 0], [10, 0], [20, 0], [30, 0], [40, 0], [50, 0]]
apple_x = randrange(-200, 180, 10)
apple_y = randrange(-180, 180, 10)
aim_x = 10
aim_y = 0

# 定义函数
def square(x,y,size,color_name):
    up()
    goto(x,y)
    down()
    color(color_name)
    begin_fill()

    forward(size)
    left(90)
    forward(size)
    left(90)
    forward(size)
    left(90)
    forward(size)
    left(90)

    end_fill()


def change(x,y):
    global aim_x,aim_y
    if aim_x+x!=0 or aim_y+y!=0:#新方向与原方向相反时，方向不变
        aim_x=x #例如，当aim_x=10时，若x=-10，判断不成立，方向不变
        aim_y=y

def inside():
    if -200<=snake[-1][0]<=180 and -190<=snake[-1][1]<=190:
        return True
    else:
        return False

def gameloop():
    global apple_x,apple_y,aim_x,aim_y,snake
    if snake[-1][0]!=apple_x or snake[-1][1]!=apple_y:
        snake.pop(0)
    else:
        apple_x=randrange(-200,180,10)
        apple_y=randrange(-180,180,10)
    if (not inside()) or crush():
        square(snake[-1][0],snake[-1][1],10,"red")
        update()
        sleep(2)
        snake=[(0,0),(10,0),(20,0),(30,0),(40,0),(50,0)]
        apple_x=randrange(-200,180,10)
        apple_y=randrange(-180,180,10)
        aim_x=10
        aim_y=0
    clear()
    square(-210,-200,410,"black")
    square(-200,-190,390,"white")
    for i in range(len(snake)):
        square(snake[i][0],snake[i][1],10,"black")
    snake.append([snake[-1][0]+aim_x,snake[-1][1]+aim_y])
    square(apple_x,apple_y,10,"red")
    ontimer(gameloop,150)
    update()

def crush():
    for n in range(len(snake)-1):
        if snake[-1][0]==snake[n][0] and snake[-1][1]==snake[n][1]:
            return True
    return False

def control():
    listen()
    onkey(lambda: change(0,10),"w")
    onkey(lambda: change(0,-10),"s")
    onkey(lambda: change(-10,0),"a")
    onkey(lambda: change(10,0),"d")


# 主程序
setup(420,420,0,0)
hideturtle()
tracer(False)
control()
gameloop()
done() 