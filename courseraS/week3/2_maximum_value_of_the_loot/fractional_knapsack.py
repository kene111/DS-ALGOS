# Uses python3
import sys
from time import time

def get_optimal_value_0(capacity, weights, values):

    value_weights =  zip(values, weights)
    weights_value_dict = {w:v for v,w in value_weights}
    units = [weights_value_dict[w]/w for w in weights_value_dict]
    units_weights =  zip(units, weights)
    units_weights_dict = {u:w for u,w in units_weights}
    units.sort(reverse=True)
    value_sum = 0
    i = 0
    n = len(units)

    while capacity != 0 and i < n:
       
        if units_weights_dict[units[i]] <= capacity:
            value_sum += weights_value_dict[units_weights_dict[units[i]]]
            capacity -= units_weights_dict[units[i]]
            i += 1 

        elif units_weights_dict[units[i]] > capacity:
            value_sum += capacity * units[i] 
            capacity = 0
            i += 1
            

            
                     
    return value_sum 


def get_optimal_value_1(capacity, weights, values):
    units = [values[i]/weights[i] for i in range(len(weights))]
    units_weights_values =  list(zip(units, weights, values))
    units_weights_values.sort(key=lambda x: x[0], reverse= True)
    value_sum = 0
    i = 0
    n = len(units)
    

    while capacity != 0 and i < n:
        unit, weight, value = units_weights_values[i]
       
        if weight <= capacity: 
            value_sum += value 
            capacity -= weight 
    
        elif weight > capacity: 
            value_sum += capacity * unit
            capacity = 0

        i += 1
            
                     
    return value_sum 


if __name__ == "__main__":
    data = list(map(int,  sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    #t0 = time()
    opt_value = get_optimal_value_1(capacity, weights, values)
    print("{:.10f}".format(opt_value))
    #print(time()-t0)


# Although both functions are the same thing,get_optimal_value_1 passess all test cases and get_optimal_value_0 doesn't.