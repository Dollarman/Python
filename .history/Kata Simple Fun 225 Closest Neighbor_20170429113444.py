
# Find closest integers above and below n that are divisible by a,b,c independently. 
from sympy.ntheory import factorint

# Example
# For n = 20, a = 2, b = 3, c = 4, the output should be [12, 24]
def closest_neighbors(n,a,b,c):
  prime_factors_abc = [factorint(a) , factorint(b) , factorint(c) ]
  # count the prime factorsDict of each (a,b,c) to find the multiplication of it
  counts = {}
  for factorsDict in prime_factors_abc:
    for factor in factorsDict:
      if factor in counts and factorsDict[factor] > counts[factor]:
        counts[factor] = factorsDict[factor]
      else:
        counts[factor] = factorsDict[factor]
  pf_abc = 1
  for factor in counts:
    pf_abc *= factor * counts[factor]  
    # local_count = {}
    # for x in factorsDict:
    #   if x in local_count:
    #     local_count[x] += 1
    #   else:
    #     local_count[x] = 1
    # for key in local_count:
    #   if key not in counts or counts[key] < local_count[key]:
    #     counts[key] = local_count[key]
  
  # pf_abc = reduce(lambda x,y: x* y, counts.keys())
  abc_fit = n / pf_abc
  left_neighbor = pf_abc * abc_fit
  right_neighbor = left_neighbor + pf_abc

  return [left_neighbor,right_neighbor]

print closest_neighbors(20,2,3,4), [12, 24]

print closest_neighbors(100,3,4,5), [60, 120]

print closest_neighbors(1000,5,10,15), [990, 1020]

print closest_neighbors(3000,7,13,31), [2821, 5642]
