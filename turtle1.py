import turtle
t=turtle.Turtle()
list1=["yellow","red","blue","green"]
t.up()
t.goto(200,0)
for i in range(4):
    t.down()
    t.begin_fill()
    t.fillcolor(list1[i])
    t.cricle(100)
    t.up()
    t.bk(100)
