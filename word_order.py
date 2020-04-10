import collections

n = int(input('integer?'))
m = list()
s = list()

for i in range(n):
    m.append(input())
j = 0
for v in range(len(m)):
    if m[0] != m[v]:
        j += 1
print(j+1)

c = collections.Counter(m)
print(len(c))
print(*c.values())