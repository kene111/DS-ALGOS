# python3
import random

# First Solution
def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0

    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])

    return max_product

# Second Solution
def max_pairwise_product_fast(numbers):

    max_1 = max(numbers)
    numbers.remove(max_1)
    max_2 = max(numbers)

    return max_1*max_2





if __name__ == '__main__':



    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]

    print(max_pairwise_product_fast(input_numbers))


"""

# Building a stress test.

    while True:
        input_n = int(random.randint(1,1000)) #input_n = int(input('Length of numbers'))
        input_numbers = [int(random.randint(0,100000)) for x in range(input_n+1)] # input_numbers = [int(x) for x in input('individual numbers').split()]
        hold1 = max_pairwise_product(input_numbers)
        hold2 = max_pairwise_product_fast(input_numbers)

        print(input_n)
        print(input_numbers)

        if hold1 != hold2:
            print(f'Something is wrong my G! check out their outputs : hold1 = {hold1} and hold2 = {hold2}')
            break

        else:
            print(f'Carry on bruh! but here are their outputs just in case: hold1 = {hold1} and hold2 = {hold2}')

        print(input_n)
        print(input_numbers)"""
