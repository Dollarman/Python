# Enter your code here. Read input from STDIN. Print output to STDOUT
''' Author: Carlos Sanchez -  cssanchez.com
These functions solve the problem of finding the minimum number of edits to equalize an array.
Using the difference between the minimum element and each elem, we can calculate the number of edits
reducing only by 5, 2, 1 pretty efficiently in a way that does not depend on the size of the input.
At the end, we must also compare to the minimum - 1 and minimum - 2 for reasons yet unknown.

ONLY POSSIBLE OPS ON EACH ITERATION:
1. She can give one chocolate to every colleague other than chosen one.
2. She can give two chocolates to every colleague other than chosen one.
3. She can give five chocolates to every colleague other than chosen one.
'''

def minNumOps(chocolates):
    localMin = min(chocolates)
    mins = [localMin, localMin - 1, localMin - 2]
    res = []
    for m in mins:
        currentRes = 0
        for c in chocolates:
            currentRes += opsToMin(c,m)
        res.append(currentRes)
    return min(res)

def opsToMin(choc,m):
    d = choc - m
    ops = 0
    while d > 0:
        if d >= 5:
            ops += d / 5 
            d = d % 5
        elif d >= 2:
            ops += d / 2
            d = d % 2
        else:
            d -= 1
            ops += 1
    return ops

# 10605
chocoTest1 = "53 361 188 665 786 898 447 562 272 123 229 629 670 848 994 54 822 46 208 17 449 302 466 832 931 778 156 39 31 777 749 436 138 289 453 276 539 901 839 811 24 420 440 46 269 786 101 443 832 661 460 281 964 278 465 247 408 622 638 440 751 739 876 889 380 330 517 919 583 356 83 959 129 875 5 750 662 106 193 494 120 653 128 84 283 593 683 44 567 321 484 318 412 712 559 792 394 77 711 977 785 146 936 914 22 942 664 36 400 857"

# 4
test2 = "2 2 3 14"

import random
mychocolateRand = str([random.randint(0,999) for x in xrange(10000)])
mychocolates = ""
for x in mychocolateRand[1:-1].split(", "):
    mychocolates += x + " "

tests = [chocoTest1, test2]
for i in xrange(len(tests)):
    chocolates = [ int(x) for x in tests[i].strip().split(" ")]
    print "test #" + str(i) + ": " + str(minNumOps(chocolates))
