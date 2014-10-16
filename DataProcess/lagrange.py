# -*- coding: utf-8 -*-
"""
Polynomial Interpolation: Lagrange's Method
Environment: Python 3.4
@author: Leonfocus
http://www.domuse.com/
"""
from functools import reduce
import operator

def lagrange(x_val, y_val, x):
    """
    Polynomial Interpolation: Lagrange's Method
    """
    def basis(i):
        l_i = [(x - x_val[j])/(x_val[i] - x_val[j]) for j in range(len(x_val)) if j != i]
        return reduce(operator.mul, l_i)*y_val[i]

    assert len(x_val) != 0 and (len(x_val) == len(y_val))

    return sum(basis(i) for i in range(len(x_val)))

# example:
x = [4, 9, 16]
y = [2, 3, 4]
print(lagrange(x, y, 11))
#3.33333...
