# Uses python3
import sys
from time import time

def get_change(m):
    #write your code here
    a = list()
    li = [10,5,1]
    i = 0
    while True:
        if sum(a) == m:
            return len(a)
        
        else:
            if sum(a)<m and m-sum(a) >= 10:
                a.append(li[i])

            if sum(a)<m and 5 <= m-sum(a) < 10: # why < 10 and not <= 10 ?
                a.append(li[i+1])

            if sum(a)<m and m-sum(a) <= 5:
                a.append(li[i+2])
                
    #return m



if __name__ == '__main__':
    m = int(input())
    #t0 = time()
    print(get_change(m))
    #print(time()-t0)
    
    
