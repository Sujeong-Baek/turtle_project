import turtle as t
import random

t.bgcolor("black")
t.speed(0)

coler1=("red","orange","lightblue","lightgreen","white","yellow","indigo","pink","hotpink")


for x in range(30):
    t.up()
    t.goto(random.randrange(-300,300),random.randrange(-300,300))
    t.down()

    t.color(random.choice(coler1))

    t.begin_fill()
    star_size=random.randint(10, 30)
    for i in range(5):
        t.forward(star_size)
        t.left(144)
    t.end_fill()

t.ht()
t.done()