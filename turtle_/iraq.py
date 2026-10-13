import turtle as t

t.pencolor('red')
t.bgcolor('#1e1e1e')
t.speed(1)
t.hideturtle()


t.fillcolor('red')

t.begin_fill()

t.forward(300)
t.right(90)
t.forward(50)
t.right(90)
t.forward(300)
t.right(90)
t.forward(50)
t.backward(50)
t.end_fill()

t.pencolor('white')
t.fillcolor('white')
t.begin_fill()
t.backward(50)
t.right(90)
t.forward(300)
t.right(90)
t.backward(50)


t.end_fill()
t.forward(50)


t.pencolor('black')
t.fillcolor('black')

t.begin_fill()


t.forward(50)
t.right(90)
t.forward(300)
t.right(90)
t.forward(50)

t.end_fill()

t.pencolor('white')

t.forward(1)
t.right(90)
t.forward(110)
t.color('green')
t.write('الله اكبر', font=('Arial', 30, 'bold'))
t.color('white')

t.backward(110)
t.color('#1e1e1e')
t.backward(190)
t.color('red')
t.write('im not arab ,im sumerian.', font=('Arial', 10, 'bold'))
t.forward(165)


t.done()