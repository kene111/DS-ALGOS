# Uses python3
import sys

def optimal_weight_0(W, w):
    # write your code here
    result = 0
    for x in w:
        if result + x <= W:
            result = result + x
    return result

def optimal_weight_1(W, w):
    # write your code here
    value = {}
    w = [0] + w
    n = len(w)
    W = W + 1
    

    # initialize

    for j in range(n+1):
        for w_p in range(W+1):
            value[w_p, j] = 0

    # fill up the array

    for i in range(1,n):
        for wn in range(1,W):
            value[wn,i] = value[wn,i-1]

            if  w[i] <= wn:
                val = value[wn- w[i],i-1] + w[i]
                if value[wn,i] < val:
                    value[wn,i] = val
    
    return value[W-1,n-1]






def optimal_weight_2(W, w):
    # write your code here
    w = [0] + w
    n = len(w)
    W = W + 1

    # initialize

    value = [[0 for _ in range(n)] for _ in range(W)]

    # fill up the array

    for i in range(1,n): 
        for wn in range(1,W):
            value[wn][i] = value[wn][i-1]

            if  w[i] <= wn:
                val = value[wn- w[i]][i-1] + w[i]
                if value[wn][i] < val:
                    value[wn][i] = val

    
    return value[W-1][n-1]



    
    

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight_2(W, w))
