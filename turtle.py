import turtle
t = turtle.Turtle()
list1=['purple','red','orange','blue','green']
for i in range(200):
    t.colour(list1[i%5])
    t.pensize(i/10+1)
    t.forward(i)
    t.left(59)
