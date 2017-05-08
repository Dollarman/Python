# Enter your code here. Read input from STDIN. Print output to STDOUT
''' ONLY POSSIBLE OPS ON EACH ITERATION:
1. She can give one chocolate to every colleague other than chosen one.
2. She can give two chocolates to every colleague other than chosen one.
3. She can give five chocolates to every colleague other than chosen one.
'''

def minNumOps(chocolates):
    localMin = min(chocolates)
    mins = [localMin]
    res = 0
    for c in chocolates:
        res += min( [opsToMin(c,m) for m in mins] ) 
    return res

def opsToMin(choc,m):
    ops = 0
    while choc > m:
        if choc - 5 >= m:
            choc -= 5
        elif choc  - 2 >= m:
            choc -= 2
        else:
            choc -= 1
        ops += 1
    return ops

# 10605
chocoTest1 = "53 361 188 665 786 898 447 562 272 123 229 629 670 848 994 54 822 46 208 17 449 302 466 832 931 778 156 39 31 777 749 436 138 289 453 276 539 901 839 811 24 420 440 46 269 786 101 443 832 661 460 281 964 278 465 247 408 622 638 440 751 739 876 889 380 330 517 919 583 356 83 959 129 875 5 750 662 106 193 494 120 653 128 84 283 593 683 44 567 321 484 318 412 712 559 792 394 77 711 977 785 146 936 914 22 942 664 36 400 857"

chocolates = [ int(x) for x in chocoTest1.strip().split(" ")]
print minNumOps(chocolates)
