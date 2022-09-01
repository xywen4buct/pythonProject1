import sys
import os

args = sys.argv[0:]

args.reverse();

#print(' '.join(args))

print(os.environ['PYTHONPATH'])

from random import *
from time import *

date1 = (2022,9,1,0,0,0,-1,-1,-1)
date2 = (2062,1,1,0,0,0,-1,-1,-1)
time1 = mktime(date1)
time2 = mktime(date2)
random_time = uniform(time1,time2)
print(asctime(localtime(random_time)))

values = list(range(1,11)) + 'Jack Queen King'.split()
ll = ['%s' %v for v in values]
print(ll)

while ll:
    input(ll.pop())