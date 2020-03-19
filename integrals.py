import numpy as np
import scipy as sp
import scipy.integrate as integrate
from scipy import signal
from scipy.integrate import dblquad


def gauss(x, sigma):
    return np.exp(-x ** 2 / (2 * sigma ** 2)) / (sigma * np.sqrt(2 * np.pi))


result = integrate.quad(lambda x: x, 0, 4.5)
print('Res for x in 0-4.5', result[0])

result = integrate.quad(lambda x: gauss(x, 1), -sp.inf, sp.inf)
print("Result of int of Gaussian func", result[0])


area = dblquad(lambda x,y: 1,0,10, lambda x:0, lambda x:10-x)
print("area of triangle with side a=10, b=10", area[0])
