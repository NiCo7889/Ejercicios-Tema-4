"""
- Desarrollar un algoritmo numérico iterativo que permita calcular el método de la bisección de una función f(x).
- Desarrollar un algoritmo numérico iterativo que permita calcular el método de la secante de una función f(x).
- Desarrollar un algoritmo numérico iterativo que permita calcular el método de Newton-Raphson de una función f(x).
- Comparar los tres algoritmos anteriores para resolver la siguiente función: x3 + x + 16 = 0, respecto de la cantidad de iteraciones necesarias por cada método para converger. 
- ¿Cuánto es la diferencia en decimales entre las distintas soluciones?
"""


import numpy as np
from scipy.misc import derivative

# Clase abstracta para los métodos
class RootFindingMethod:
    def __init__(self, function, tol=1e-6, max_iter=1000):
        self.function = function
        self.tol = tol
        self.max_iter = max_iter

    def find_root(self):
        raise NotImplementedError

# Método de Bisección
class BisectionMethod(RootFindingMethod):
    def __init__(self, function, a, b, tol=1e-6, max_iter=1000):
        super().__init__(function, tol, max_iter)
        self.a = a
        self.b = b

    def find_root(self):
        a, b = self.a, self.b
        for _ in range(self.max_iter):
            c = (a + b) / 2.0
            if self.function(c) == 0 or abs(b - a) < self.tol:
                return c
            elif np.sign(self.function(c)) == np.sign(self.function(a)):
                a = c
            else:
                b = c
        return c  # Regresa la última estimación si no se encontró la raíz

# Método de Secante
class SecantMethod(RootFindingMethod):
    def __init__(self, function, a, b, tol=1e-6, max_iter=1000):
        super().__init__(function, tol, max_iter)
        self.a = a
        self.b = b

    def find_root(self):
        x0, x1 = self.a, self.b
        for _ in range(self.max_iter):
            x2 = x1 - (self.function(x1) * (x1 - x0)) / (self.function(x1) - self.function(x0))
            if abs(x2 - x1) < self.tol:
                return x2
            x0, x1 = x1, x2
        return x2

# Método de Newton-Raphson
class NewtonMethod(RootFindingMethod):
    def __init__(self, function, x0, tol=1e-6, max_iter=1000):
        super().__init__(function, tol, max_iter)
        self.x0 = x0

    def find_root(self):
        x = self.x0
        for _ in range(self.max_iter):
            f_x = self.function(x)
            f_prime_x = derivative(self.function, x, dx=1e-6)
            x_new = x - f_x / f_prime_x
            if abs(x_new - x) < self.tol:
                return x_new
            x = x_new
        return x_new

# Función para comparar métodos
def compare_methods(function, a, b, x0):
    methods = [BisectionMethod(function, a, b), SecantMethod(function, a, b), NewtonMethod(function, x0)]
    roots = []
    for method in methods:
        root = method.find_root()
        roots.append(root)
        print(f"El método {method.__class__.__name__} converge a la raíz {root}.")

    # Diferencia en decimales entre las soluciones
    print("\nDiferencias entre las soluciones:")
    for i in range(len(roots)):
        for j in range(i+1, len(roots)):
            print(f"Diferencia entre {methods[i].__class__.__name__} y {methods[j].__class__.__name__}: {abs(roots[i]-roots[j])}")

# Función objetivo
def function(x):
    return x**3 + x + 16

# Comparar métodos
compare_methods(function, -10, 10, 1)
