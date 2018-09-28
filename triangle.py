import turtle

painter = turtle.Turtle()

for _ in range(3):
    painter.forward(100)
    painter.left(3)

for _ in range(20):
    painter.forward(100)
    painter.left(100)

turtle.done()
print('hello worla')