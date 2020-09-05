# Uses python3
import sys
import random

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current
    return sum % 10

def pisanoperiod():
    m = 10 
    previous, current = 0, 1
    for i in range(0, m * m): 
        previous, current = current, (previous + current) % m 
        
          
        # A Pisano Period starts with 01 
        if (previous == 0 and current == 1): 
            return i + 1




def fibonacci_sum_fast(n):

    n = n %  60 #pisanoperiod()
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, (previous  + current) % 10 
        sum += (current % 10 )
    
    return sum  % 10

if __name__ == '__main__':

    n = int(input())
    print(fibonacci_sum_fast(n))

''' # stress test
    while True:
        input_n = int(random.randint(1,10)) 
        hold1 = fibonacci_sum_naive(input_n)
        hold2 = fibonacci_sum_fast(input_n)

        if hold1 != hold2:
            print(f'Something is wrong my G! check out their outputs : hold1 = {hold1} and hold2 = {hold2}')
            break

        else:
            print(f'Carry on bruh! but here are their outputs just in case: hold1 = {hold1} and hold2 = {hold2}')

'''
