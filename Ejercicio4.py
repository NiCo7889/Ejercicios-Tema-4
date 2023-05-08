"""
- Desarrollar un algoritmo numérico iterativo que permita calcular el método de la bisección de una función f(x).
- Desarrollar un algoritmo numérico iterativo que permita calcular el método de la secante de una función f(x).
- Desarrollar un algoritmo numérico iterativo que permita calcular el método de Newton-Raphson de una función f(x).
- Comparar los tres algoritmos anteriores para resolver la siguiente función: x3 + x +16 = 0, respecto de la cantidad de iteraciones necesarias por cada método para converger. 
- ¿Cuánto es la diferencia en decimales entre las distintas soluciones?
"""

import math

class MetodoNumerico:
    def __init__(self, func, tol=1e-6, max_iter=100):
        self.func = func
        self.tol = tol
        self.max_iter = max_iter

    def resolver(self):
        raise NotImplementedError


class Biseccion(MetodoNumerico):
    def __init__(self, func, a, b, tol=1e-6, max_iter=100):
        super().__init__(func, tol, max_iter)
        self.a = a
        self.b = b

    def resolver(self):
        a, b = self.a, self.b
        for i in range(self.max_iter):
            c = (a + b) / 2
            if self.func(c) == 0 or (b - a) / 2 < self.tol:
                return c, i + 1
            if self.func(a) * self.func(c) < 0:
                b = c
            else:
                a = c
        return None, None


class Secante(MetodoNumerico):
    def __init__(self, func, x0, x1, tol=1e-6, max_iter=100):
        super().__init__(func, tol, max_iter)
        self.x0 = x0
        self.x1 = x1

    def resolver(self):
        x0, x1 = self.x0, self.x1
        for i in range(self.max_iter):
            x2 = x1 - self.func(x1) * (x1 - x0) / (self.func(x1) - self.func(x0))
            if abs(x2 - x1) < self.tol:
                return x2, i + 1
            x0, x1 = x1, x2
        return None, None


class NewtonRaphson(MetodoNumerico):
    def __init__(self, func, deriv, x0, tol=1e-6, max_iter=100):
        super().__init__(func, tol, max_iter)
        self.deriv = deriv
        self.x0 = x0

    def resolver(self):
        x = self.x0
        for i in range(self.max_iter):
            x_new = x - self.func(x) / self.deriv(x)
            if abs(x_new - x) < self.tol:
                return x_new, i + 1
            x = x_new
        return None, None


def comparar_metodos(f, df, a, b, x0, x1):
    biseccion = Biseccion(f, a, b).resolver()
    secante = Secante(f, x0, x1).resolver()
    newton_raphson = NewtonRaphson(f, df, x0).resolver()

    print("Bisección: Raíz = {:.6f}, Iteraciones = {}".format(*biseccion))
    print("Secante: Raíz = {:.6f}, Iteraciones = {}".format(*secante))
    print("Newton-Raphson: Raíz = {:.6f}, Iteraciones = {}".format(*newton_raphson))

    diff_bs = abs(biseccion[0] - secante[0])
    diff_bn = abs(biseccion[0] - newton_raphson[0])
    diff_sn = abs(secante[0] - newton_raphson[0])

    print("Diferencia en decimales entre Bisección y Secante: {:.10f}".format(diff_bs))
    print("Diferencia en decimales entre Bisección y Newton-Raphson: {:.10f}".format(diff_bn))
    print("Diferencia en decimales entre Secante y Newton-Raphson: {:.10f}".format(diff_sn))

def f(x):
    return x**3 + x + 16

def df(x):
    return 3*x**2 + 1

a, b = -5, 5
x0, x1 = -5, 5

comparar_metodos(f, df, a, b, x0, x1)

