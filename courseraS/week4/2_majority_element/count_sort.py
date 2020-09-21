#-----------------------------------------------------COUNT SORT----------------------------------------------------------------------------------
def count_sort(a):
    l = len(a) # length of  list a
    m = max(a) + 3 # max element in list a plus a random number, i choose 3
    check = [0] * l # output
    count = [0] * m
    # store the count of each element in a, at the elements index position in count
    for i in a:
        count[i] +=  1
    # store the cummulative count
    for i in range(1, m):
        count[i] += count[i-1]
    # find the index of each of the element of the original array (a) in the count array
    # place the elements in the output array

    i =  l - 1
    while i>=0:
        check[count[a[i]] - 1 ] = a[i]
        count[a[i]] -= 1
        i -= 1

    for i in range(0, l):
        a[i] = check[i]
        
    return a