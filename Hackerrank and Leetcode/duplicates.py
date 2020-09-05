lis = [2, 4, 6, 8, 10, 2, 6, 10]

def singles(lis):
    lis = sorted(lis)
    dict = {}
    new_lis = []

    for i in lis:
        if i not in dict:
            dict[i] = 0
        dict[i]+= 1

    for v in dict:
        if dict[v] == 1:
            new_lis.append(v)
            return(new_lis)



check = singles(lis)
print(check)










