# Uses python3
import random
import sys

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n-1):
        previous, current = current, previous + current
        #print(f' previous ==>{previous}, current==>{current}')

    return current % 10

def get_fibonacci_last_digit_fast(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n-1):
        previous, current = current, previous % 10 + current % 10
        #print(f' previous ==>{previous}, current==>{current}')

    return current % 10


if __name__ == '__main__':
    n = int(input())
    print(get_fibonacci_last_digit_fast(n))

    # Building a stress test.
'''
    while True:
        input_n = int(random.randint(1,10000)) 
        hold1 = get_fibonacci_last_digit_naive(input_n)
        hold2 = get_fibonacci_last_digit_fast(input_n)

        if hold1 != hold2:
            print(f'Something is wrong my G! check out their outputs : hold1 = {hold1} and hold2 = {hold2}')
            break

        else:
            print(f'Carry on bruh! but here are their outputs just in case: hold1 = {hold1} and hold2 = {hold2}')

'''