from fnmatch import *
from math import log
def f(x):
    d = set()
    for i in range(1,int(x**0.5)+1):
        if x % i ==0:
            d |= {i,x//i}
    return log(len(d),2) == int(log(len(d),2))
for x in range(0, 10**9+1, 2031*31):
    if fnmatch(str(x), '*31*65?'):
        print(x,x//2031)