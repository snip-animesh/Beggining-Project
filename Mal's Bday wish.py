import turtle

maliha = turtle.Screen()
maliha.bgcolor("palegreen")
MiQuerida = turtle.Turtle()
MiQuerida.width(8)
colors = ["#f5ac2f", "#279cf5", "#d820f5", "#a2f52f", "#f527c1"]


def draw_MyG(_, x, y):
    MiQuerida.pencolor("mistyrose")
    MiQuerida.color(colors[_ % 7])
    MiQuerida.lt(70)
    MiQuerida.penup()
    MiQuerida.goto(x, y)
    MiQuerida.pendown()
    MiQuerida.circle(22)
    MiQuerida.end_fill()


def ballon(x, y):
    MiQuerida.pensize(4)
    for i in range(5):
        draw_MyG(i, x, y)


def cake(x, y):
    MiQuerida.fd(x)
    MiQuerida.rt(90)
    MiQuerida.fd(y)
    MiQuerida.rt(90)
    MiQuerida.fd(x)
    MiQuerida.rt(90)
    MiQuerida.fd(y)


def move(x, y):
    MiQuerida.up()
    MiQuerida.setposition(0, 0)
    MiQuerida.setheading(90)
    MiQuerida.lt(90)
    MiQuerida.fd(x)
    MiQuerida.rt(90)
    MiQuerida.fd(y)
    MiQuerida.pendown()


def A(size):
    MiQuerida.rt(19)
    MiQuerida.forward(size)
    MiQuerida.rt(141)
    MiQuerida.fd(size)
    MiQuerida.backward(size / 2)
    MiQuerida.rt(105)
    MiQuerida.fd(int(size / 3))


def B(size):
    MiQuerida.forward(size)
    MiQuerida.rt(90)
    for i in range(18):
        MiQuerida.rt(9)
        MiQuerida.fd(size // 20)
    for i in range(18):
        MiQuerida.rt(size // 5)
        MiQuerida.backward(size // 20)


def D(size):
    MiQuerida.fd(size)
    MiQuerida.rt(90)
    MiQuerida.fd(size // 10)
    for i in range(13):
        MiQuerida.rt(13)
        MiQuerida.fd(size // 8)


def E(size):
    MiQuerida.rt(90)
    MiQuerida.fd(int(size / 3))
    MiQuerida.back(int(size / 3))
    MiQuerida.left(90)
    MiQuerida.fd(size / 2)
    MiQuerida.rt(90)
    MiQuerida.fd(int(size / 3))
    MiQuerida.back(int(size / 3))
    MiQuerida.lt(90)
    MiQuerida.fd(size / 2)
    MiQuerida.rt(90)
    MiQuerida.fd(int(size / 3))


def H(size):
    MiQuerida.fd(size)
    MiQuerida.backward(size // 2)
    MiQuerida.rt(90)
    MiQuerida.fd(size // 2)
    MiQuerida.lt(90)
    MiQuerida.fd(size // 2)
    MiQuerida.backward(size)


def I(size):
    MiQuerida.right(90)
    MiQuerida.fd(size)
    MiQuerida.backward(size//2)
    MiQuerida.left(90)
    MiQuerida.fd(size)
    MiQuerida.rt(90)
    MiQuerida.fd(size//2)
    MiQuerida.backward(size)
    # MiQuerida.circle(size // 8)

def L(size):
    MiQuerida.rt(90)
    MiQuerida.fd(int(size / 2))
    MiQuerida.back(int(size / 2))
    MiQuerida.lt(90)
    MiQuerida.fd(size)

def N(size):
    MiQuerida.fd(size)
    MiQuerida.rt(150)
    MiQuerida.fd(size + int(size / 6))
    MiQuerida.lt(150)
    MiQuerida.fd(size)


def P(size):
    MiQuerida.fd(size)
    MiQuerida.rt(90)
    MiQuerida.fd(size // 8)
    for i in range(8):
        MiQuerida.rt(20)
        MiQuerida.fd(size // 9)

def R():
    MiQuerida.fd(60)
    MiQuerida.rt(90)
    MiQuerida.fd(7)
    for i in range(15):
        MiQuerida.rt(12)
        MiQuerida.fd(3)
    MiQuerida.lt(120)
    MiQuerida.fd(40)


def S(size):
    MiQuerida.rt(90)
    for i in range(0, 5):
        if i < 3:
            MiQuerida.fd(size / 2)
            MiQuerida.lt(90)
            if i == 2:
                MiQuerida.rt(90)
        else:
            MiQuerida.right(90)
            MiQuerida.fd(size / 2)


def T(size):
    MiQuerida.fd(size)
    MiQuerida.rt(90)
    MiQuerida.fd(size // 2)
    MiQuerida.backward(size)


def Y(size):
    MiQuerida.fd(size)
    MiQuerida.left(60)
    MiQuerida.fd(size // 2)
    MiQuerida.backward(size // 2)
    MiQuerida.rt(90)
    MiQuerida.fd(size // 1.5)


def M(size):
    MiQuerida.forward(size)
    MiQuerida.right(135)

    MiQuerida.forward(size//2)
    MiQuerida.left(90)
    MiQuerida.forward(size // 2)
    MiQuerida.right(135)
    MiQuerida.forward(size)


MiQuerida.speed(7)
move(120, 30)
MiQuerida.color("violet")
MiQuerida.begin_fill()
cake(40, 180)
MiQuerida.end_fill()
move(110, 75)
MiQuerida.color("aqua")
MiQuerida.begin_fill()
cake(40, 160)
MiQuerida.end_fill()
move(100, 120)
MiQuerida.color("salmon")
MiQuerida.begin_fill()
cake(40, 140)
MiQuerida.end_fill()
move(30, 170)
MiQuerida.width(11)
MiQuerida.pencolor("red")
MiQuerida.circle(6)
maliha.bgcolor("seashell")
move(180, 307)
move(0, 0)
MiQuerida.speed(15)
ballon(-490, 200)
ballon(490, 200)
ballon(183, -150)
ballon(-133, -150)

MiQuerida.speed(1)
MiQuerida.width(10)
MiQuerida.pencolor("turquoise2")
move(270, 205)
M(70)
MiQuerida.speed(5)
MiQuerida.pencolor("violetred2")
move(200, 205)
A(70)
MiQuerida.pencolor("turquoise2")
move(130, 205)
L(size=70)
MiQuerida.pencolor("violetred2")
move(80, 205)
MiQuerida.speed(2)
I(size=70)
MiQuerida.speed(5)
MiQuerida.pencolor("turquoise2")
move(-5, 205)
H(size=70)
MiQuerida.pencolor("violetred2")
move(-60, 205)
A(size=70)

MiQuerida.speed(9)
maliha.bgcolor("wheat1")
MiQuerida.pencolor("yellowgreen")
MiQuerida.width(13)
move(260, -80)
H(100)
MiQuerida.pencolor("cyan")
MiQuerida.width(7)
MiQuerida.speed(1)
move(190, -80)
A(65)
MiQuerida.speed(10)
move(135, -80)
P(60)
move(100, -80)
P(60)
MiQuerida.pencolor("turquoise4")
move(52, -80)
MiQuerida.speed(5)
Y(60)
MiQuerida.pencolor("cyan")
MiQuerida.speed(10)
move(10, -80)
B(60)
move(-30, -80)
I(60)
move(-100, -80)
R()
move(-150, -80)
T(100)
move(-200, -80)
H(60)
move(-300, -80)
MiQuerida.pencolor('hotpink')
MiQuerida.speed(3)
D(200)
MiQuerida.pencolor("turquoise3")
move(-305, -80)
MiQuerida.speed(7)
A(60)
MiQuerida.pencolor("turquoise")
move(-370, -80)
Y(50)
maliha.exitonclick()
