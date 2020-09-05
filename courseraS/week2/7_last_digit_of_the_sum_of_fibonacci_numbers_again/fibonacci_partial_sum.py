# Uses python3
import sys
import random

def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next  = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

    return sum % 10


def fibonacci_partial_sum_fast(from_, to):

    from_ = from_ % 60
    to =  to % 60

    sum = 0

    current = 0
    next  = 1

    for i in range(to + 1):
        if i >= from_:
            sum += (current) % 10

        current, next = next, (current + next) % 10

    return sum % 10


if __name__ == '__main__':
    #n = input()
    #from_, to = map(int, n.split())
    #print(fibonacci_partial_sum_fast(from_, to))

 # stress test
    while True:
        n,m = int(random.randint(1,10000)), int(random.randint(10000,100000))
        print(f' n ==> {n} and m ==> {m}')
        hold1 = fibonacci_partial_sum_naive(n,m)
        hold2 = fibonacci_partial_sum_fast(n,m)

        if hold1 != hold2:
            print(f'Something is wrong my G! check out their outputs : hold1 = {hold1} and hold2 = {hold2}')
            break

        else:
            print(f'Carry on bruh! but here are their outputs just in case: hold1 = {hold1} and hold2 = {hold2}')


