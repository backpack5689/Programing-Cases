# 3 non-negative integers, e, f, c
# e - empty soda bottles at start of day - e < 1000
# f - empty soda bottles found during day - f < 1000
# c - number of empty bottles required for new soda - 2 <= c <= 2000
# extra thirsty day - drank all sodas until couldn't afford more
from math import floor

data = [int(a) for a in input().split()]
e = data[0]
f = data[1]
soda_cost = data[2]

sodas_empty = e + f 
sodas_drank = 0
sodas_full = 0
while not sodas_empty < soda_cost:
    sodas_full = floor(sodas_empty / soda_cost)
    sodas_empty = (sodas_empty % soda_cost) + sodas_full
    sodas_drank += sodas_full
    
print(sodas_drank)
