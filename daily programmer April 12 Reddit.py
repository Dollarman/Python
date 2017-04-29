# INPUT:
#
# a * root(b)
# ------
# c * root(d)

def perfect_squares_up_to(n):
    x = 4
    counter = 1
    perfect_squares = []
    while x < n:
        perfect_squares.append(x)
        x += 2 * counter + 1
        counter++
    return perfect_squares

def prime_factor(n):
    if n == 2:
        return 2

    factors = []
    fac = 2
    lastFac = 0
    mynum = n

    while fac < mynum:
        if mynum % fac == 0:
            factors.append(fac)
            fac = 2
            mynum /= fac
        elif fac > mynum / 2 + 1:
            break
        else:
            fac +=  1

    return factors

def solve(a,b,c,d):
    top_fraction = prime_factor(a)
    bottom = prime_factor(c)
    top_remove = []
    bottom_remove = []
    for x in range(top):
        if x in bottom:
            top.remove(x)
            bottom.remove(x)
