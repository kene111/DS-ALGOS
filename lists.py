N = int(input())
my_list = []


for i in range(N):
    c = input().split()

    if c[0] == 'insert':
        my_list.insert(int(c[1]), int(c[2]))

    elif c[0] == 'print':

        print(my_list)

    elif c[0] == 'remove':

        my_list.remove(int(c[1]))

    elif c[0] == 'append':

        my_list.append(int(c[1]))

    elif c[0] == 'sort':
        my_list.sort()

    elif c[0] == 'pop':
        my_list.pop()

    elif c[0] == 'reverse':
        my_list.reverse()

