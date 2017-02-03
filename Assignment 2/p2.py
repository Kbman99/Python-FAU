import pylab
import math

while True:
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))

    under_the_root = float(b * b - (4 * a * c))

    if under_the_root < 0:
        print("No real solutions")
    elif under_the_root == 0:
        x_1 = (-b)/(2 * a)
        print("One solution: {0}".format(x_1))
    else:
        x_1 = (-b + math.sqrt(under_the_root))/(2 * a)
        x_2 = (-b - math.sqrt(under_the_root))/(2 * a)
        print("Two solutions: x1 = {0}".format(x_1) + ", x2 = {0}".format(x_2))

    x = pylab.linspace(-5, 5, 100)
    quad_form = a * x * x + b * x + c
    pylab.plot(x, quad_form, '-bo')
    pylab.grid()
    pylab.show()
