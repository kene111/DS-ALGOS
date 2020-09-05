# Uses python3
import sys
import random

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

def gcd_naive_fast(a, b):
    if  b == 0:
        return a
    else:
        a_prime =  a%b # the reminder of a divided by b


    return gcd_naive_fast(b, a_prime)

def lcm_fast(a, b):
    gcd = gcd_naive_fast(a, b)
    a_ =  a / gcd
    lcm =  b * a_
    
    return int(lcm)



if __name__ == '__main__':
    inp = input()
    a, b = map(int, inp.split())
    print(lcm_fast(a, b))
'''
    while True:
        a,b = int(random.randint(1,1000)),int(random.randint(1,1000))  
        hold1 = lcm_naive(a,b)
        hold2 = lcm_fast(a,b)

        if hold1 != hold2:
            print(f'Something is wrong my G! check out their outputs : hold1 = {hold1} and hold2 = {hold2}')
            break

        else:
            print(f'Carry on bruh! but here are their outputs just in case: hold1 = {hold1} and hold2 = {hold2}')


'''