# This code prints out the second runner up if there are no duplicates

n = input('type')

arr = list(map(int, input().split()))

max_num = max(arr)

for i in arr:
    if i == max_num:
        arr.remove(max_num)


print(max(arr))


# This code prints out the second runner up if there are duplicates

n = input('type')

arr = list(map(int, input().split()))

max_num = max(arr)

m = len(arr)
# For some weird reason the code runs better when you set m = len(arr)

i = 0
while i <= m:
    if max_num == max(arr):
        arr.remove(max_num)
    i += 1

print(max(arr))






