import math

def getTotalX(a, b):
    count = 0
    start, end = math.lcm(*a), math.gcd(*b)
    
    for i in range(start, end+1, start):
        if end % i == 0:
            count += 1

    return count
