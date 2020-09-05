array = [1, 2, 5, 0, 6, 7, 8, 0, 4, 2, 3, 4, 5]

""" works for one zero
def move(lis):
    g = len(lis)
    m = g-1
    i = 0
    while True:
        if lis[i] == 0:
            lis[i] = lis[i+1]
            lis[i+1] = 0
        i += 1

        if lis[m] == 0:
            return(lis) 
"""
# Using samad's method

array[:] = [x for x in array if x != 0] + [0]*array.count(0)


print(array)