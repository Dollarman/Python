
# Find closest integers above and below n that are divisible by a,b,c independently. 
from sympy.ntheory import factorint
import set

def closest_neighbors(n,a,b,c):
  prime_factors_abc = set( factorint(a).keys() + factorint(b).keys() + factorint(c).keys())