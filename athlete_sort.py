import operator
nm = input().rstrip().split()

n = int(nm[0])
m = int(nm[1])

arr = []

for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))


k = int(input())

for tick in sorted(arr, key=operator.itemgetter(k)): # or you could say key=lambda v: v[k]

    print(*tick)



