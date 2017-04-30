// List of primes less than 100: [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89, 97]





function closest_neighbors(n,a,b,c) {

}

function factors(x) {
  primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97];
  myX = x;
  factors = {};
  while (myX > 1) {
    for (prime in primes) {
      if (prime % myX == 0) {
        if (prime in factors) {
          factors[prime] += 1
        } else {factors[prime] = 1}
        myX /= prime;
        break;
    }  
    }
  }
}