# Uses python3
import sys
import math


# --------------------------------------------- re-edit count sort algorithm 1 ------------------------------------------------------------------------
def count_sort_re_0(a):
    l = max(a) + 3 
    count = [0] * l
    # store the count of each element in a, at the elements index position in count
    for i in a:
        count[i] +=  1

    return count

# ------------------------------------------------------------------------------------------------------------------------------------------------
def get_majority_element(a, left, right):  # works but takes up memory.

    see = count_sort_re_0(a)

    if left == right:
        return -1

    if left + 1 == right:
        return a[left]

    # write your code here
    hold = max(see)
    if hold > right/2:

        return see.index(hold)
        
    elif hold <= right/2:
        return -1



# --------------------------------------------- re-edit count sort algorithm 2 ------------------------------------------------------------------------
def count_sort_re_1(a): 
    
    count_a = {a_n: 0 for a_n in a}
    
    for i in a:
        count_a[i] +=  1
    return count_a


#-------------------------------------------------------------------------------------------------------------------------------------------------
def get_majority_element_1(a, left, right):

    see = count_sort_re_1(a)

    if left == right:
        return -1

    if left + 1 == right:
        return a[left]
    
    # write your code here

    for i in see.keys():
        
        if see[i] > right/2:
            return i
    
    return -1

    
    
    

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element_1(a, 0, n) != -1:
        print(1)
    else:
        print(0)
