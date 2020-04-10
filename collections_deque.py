from collections import deque
n = int(input())
d = deque()

for i in range(n):
    m = input().split()

    if m[0] == 'append':
        d.append(m[1])

    if m[0] == 'appendleft':
        d.appendleft(m[1])

    if m[0] == 'pop':
        d.pop()

    if m[0] == 'popleft':
        d.popleft()

print(*d)
