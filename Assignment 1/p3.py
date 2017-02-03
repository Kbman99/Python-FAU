import pylab
import math


def compute_interval(min, max, number_of_samples):
    while max > min:
        sample_points = []
        interval_separation = float((max - min)/number_of_samples)
        for i in range(number_of_samples):
            sample_points.append(round(max - i*interval_separation, 4))
        return sample_points
    print("The maximum value must be larger than the minimum value!")


def evaluate_func(sample_points, function):
    while sample_points:
        func_values = []
        for x in sample_points:
            y = eval(function)
            func_values.append(round(y, 4))
        return func_values


def setup_table_and_graph():
    print("             x              y")
    print("-----------------------------")
    for i in range(ns):
        print("     {: 9.4f}      {: 9.4f}".format(xs[i], ys[i]))
    pylab.xlabel("x")
    pylab.ylabel("y")
    pylab.title(fun_str)
    pylab.plot(xs, ys, '-bo')
    pylab.grid()
    pylab.show()


while True:
    fun_str = input("Pleas enter a function using x as the variable: ")
    x_min = float(input("Enter a Minimum value for x: "))
    x_max = float(input("Enter a Maximum value for x: "))
    ns = int(input("How many samples would you like to use: "))
    xs = compute_interval(x_min, x_max, ns)
    ys = evaluate_func(xs, fun_str)
    setup_table_and_graph()
