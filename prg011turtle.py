import turtle

t = turtle.Turtle()
t.speed(1)

for _ in range(10):
    t.forward(20)
    t.right(90)
    t.forward(20)
    t.left(90)

turtle.done()