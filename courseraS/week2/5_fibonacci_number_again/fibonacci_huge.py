# Uses python3
import sys
import random

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous+ current 

    return current % m


def pisanoperiod(m): 
    previous, current = 0, 1
    for i in range(0, m * m): 
        previous, current = current, (previous + current) % m 
        
          
        # A Pisano Period starts with 01 
        if (previous == 0 and current == 1): 
            return i + 1

def get_fibonacci_huge_fast(n, m):
    

    n = n % pisanoperiod(m)

    if n <= 1:
        return n

    previous = 0
    current  = 1

    
    for _ in range(n - 1):
        previous, current = current, previous  + current 

    return current % m


if __name__ == '__main__':

    n = input()
    n, m = map(int, n.split())
    print(get_fibonacci_huge_fast(n, m))
    


"""

    while True:
        n, m = random.randint(1,1000) , random.randint(2,1000)
        
        hold1 = get_fibonacci_huge_naive(n, m)
        hold2 = get_fibonacci_huge_fast(n, m)

        if hold1 != hold2:
            print(f'Something is wrong my G! check out their outputs : hold1 = {hold1} and hold2 = {hold2}')
            break

        else:
            print(f'Carry on bruh! but here are their outputs just in case: hold1 = {hold1} and hold2 = {hold2}')

"""