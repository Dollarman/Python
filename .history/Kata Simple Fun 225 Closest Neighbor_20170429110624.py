
# Find closest integers above and below n that are divisible by a,b,c independently. 
from sympy.ntheory import factorint
import set
# Example
# For n = 20, a = 2, b = 3, c = 4, the output should be [12, 24]
def closest_neighbors(n,a,b,c):
  prime_factors_abc = sorted(set( factorint(a).keys() + factorint(b).keys() + factorint(c).keys() ))
  pf_abc = reduce(lambda x,y: x* y, prime_factors_abc)
  abc_fit = n / pf_abc
  left_neighbor = pf_abc * abc_fit
  right_neighbor = left_neighbor + pf_abc
