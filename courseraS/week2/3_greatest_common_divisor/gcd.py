# Uses python3
import sys
'''
def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd

'''
def gcd_naive_fast(a, b):
    if  b == 0:
        return a
    else:
        a_prime =  a%b # the reminder of a divided by b


    return gcd_naive_fast(b, a_prime)


if __name__ == "__main__":

    #inputs = int(input()) #sys.stdin.read()
    a, b = map(int, input().split())
    print(gcd_naive_fast(a, b))