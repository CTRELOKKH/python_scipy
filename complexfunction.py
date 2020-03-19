import scipy as sp
import numpy as np
from scipy import linalg


def norm(start, end, number_of_elements):
    xs = np.linspace(start, end, number_of_elements)
    return linalg.norm(xs)


print(norm(2, 7, 100))


def find_max_norm(start_range, end_range, number_of_elements):
    maximum = 0
    for i in start_range:
        for j in end_range:
            x = norm(i, j, number_of_elements)
            if x > maximum:
                maximum = x
    return maximum


print(find_max_norm(np.linspace(0, 1, 10), np.linspace(0, 5, 10),100))
