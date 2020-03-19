from scipy.stats import binom
import scipy as sp
import numpy as np

n,p = 50, .25

x = np.linspace(0,50,51)
correct_answer_points = 2
wrong_answer_points = -1
correct_answer = binom.pmf(x, n, p)

print('Probabilities for exact number of correct answer:')
print(correct_answer)
print('Sum of probabilities: ', sum(correct_answer))
print('Expected points (out of 100):', binom.mean(n,p)*correct_answer_points)


wrong_answers = binom.pmf(x,n,1-p)
print('Probabilities for exact number of wrong answer:')
print(wrong_answers)
print('Sum of probabilities: ', sum(wrong_answers))


