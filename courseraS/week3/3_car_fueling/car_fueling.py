# python3
import sys


def compute_min_refills(distance, tank, stops):
    # write your code here
    nr,cr = 0,0 # nr: number of refill, cr: current refill
    stops.append(distance)
    stops = [0] + stops
    n = len(stops) - 2 # 4
    
    # stops = 200 375 550 750 950  : 400
    # stops = 1 2 5 9           : 3
    while cr <= n:
        lr = cr # lr: last refill
        while cr <= n and stops[cr+1] - stops[lr] <= tank :
            cr += 1
            
        if cr == lr:
            return(-1) # IMPOSSIBLE

        if cr <= n:
            nr += 1
    
    return(nr)

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
