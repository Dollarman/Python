// List of primes less than 100: [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89, 97]

function closest_neighbors(n,a,b,c) {
  var prime_factors_abc = [factorize(a) , factorize(b) , factorize(c) ];
  // count the prime factorsDict of each (a,b,c) to find the multiplication of it
  var counts = {};
  for (factorsDict in prime_factors_abc){
    for (factor in factorsDict) {
      if (factor in counts && factorsDict[factor] > counts[factor])
        {counts[factor] = factorsDict[factor];}
      else {counts[factor] = factorsDict[factor]}
    }
  }
  var pf_abc = 1;
  for (factor in counts) {
    pf_abc *= factor * counts[factor];
  }
  var abc_fit = n / pf_abc;
  var left_neighbor = pf_abc * abc_fit;
  var right_neighbor = left_neighbor + pf_abc;

  return [left_neighbor,right_neighbor];
}
// I will only factorize ints between 1 and 100.
function factorize(x) {
  var primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97];
  var myX = x;
  var factors = {};
  while (myX > 1) {
    for (prime in primes) {
      if (prime > myX) {break;}
      if (myX % prime == 0) {
        if (prime in factors) {
          factors[prime] += 1;
        } else {
          factors[prime] = 1;
        }
        myX /= prime;
        break;
      }
    }
  }
return factors;
}
console.log(factorize(2));
console.log(factorize(3));
console.log(factorize(4));
console.log("got: " + closest_neighbors(20,2,3,4) + " expected: " + "[12,24]");