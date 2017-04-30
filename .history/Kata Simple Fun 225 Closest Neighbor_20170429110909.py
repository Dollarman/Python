
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

print closestNeighbor(20,2,3,4), [12, 24]

print closestNeighbor(100,3,4,5), [60, 120]

print closestNeighbor(1000,5,10,15), [990, 1020]

print closestNeighbor(3000,7,13,31), [2821, 5642]
