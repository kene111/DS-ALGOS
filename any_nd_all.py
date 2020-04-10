m, v = int(input()), input().split()
print(all(int(i) >= 0 for i in v) and any(j == j[::-1] for j in v))
