a=[17,28,30]
b=[99,16,8]


def compareTriplets(a,b):
    a_d = 0
    b_e = 0
    c= zip(a,b)
    for i,j in c:
        if i > j:
            a_d += 1
        if j > i:
            b_e += 1
        if i == j:
            pass

    return([a_d,b_e])


print(compareTriplets(a,b))





