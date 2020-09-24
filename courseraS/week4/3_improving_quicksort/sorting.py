# Uses python3
import sys
import random
from time import time

def partition3(a, l, r):
    #write your code here
    x = a[l]
    j = l

    for i in range(l + 1, r + 1 ):
        if  a[i] <= x: 
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l] 

    #print(a)         
    
    main = j
    curr = j
    for i in range(l, j):
        if a[i] == a[j] and i < j:
            curr -= 1
            a[i],a[curr] = a[curr], a[i]
            j -= 1

                   
    return curr, main

''' This while loop works perfectly but still isn't as fast enough for very large arrays

    while l < j:
        if a[l] == a[j]:
            if a[j] - a[l] == 0:
                return curr, j
            curr -= 1
            a[l],a[curr] = a[curr], a[l]
        l += 1
    return curr, j

'''

    
'''
def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j
'''

def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    d, u = partition3(a, l, r)
    #m = partition2(a, l, r)
    randomized_quick_sort(a, l, d - 1);
    randomized_quick_sort(a, u + 1, r);
'''
q = [5,5,4,3,2,1]
#q = [9,2,2,9,3,9,6,7,9]
w = len(q) - 1

print(partition3(q,0,w))
print(q)

'''
if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    #t0 = time()
    for x in a:
        print(x, end=' ')
    #print(' ')
   # print(time() - t0)










# a = [ 3, 4 , 2, 2, 2 , 2] k = index 2

# when 
# a = [ 2, 4 , 3, 2, 2 , 2] j= 0


# a = [ 2, 2, 3, 4, 2, 2] j = 1
# a = [ 2, 2, 2, 4, 3, 2] j = 2
# a = [ 2, 2, 2, 2, 3, 4] j = 3