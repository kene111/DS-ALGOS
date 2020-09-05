# Uses python3

def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)


def calc_fib_fast(n):

    if n <= 1:
        return n

    flist = list()
    flist.append(0)
    flist.append(1)

    for num in range(2,n+1):
        flist.append(flist[num - 1] + flist[num - 2])

    return flist#[n]9

n = int(input())
print(calc_fib_fast(n))
'''

flist = list()
flist.append(0)
flist.append(1)
flist.append(flist[2 - 1]+ flist[2 - 2])
flist.append(flist[3 - 1]+ flist[3 - 2])
flist.append(flist[4 - 1]+ flist[4 - 2])
flist.append(flist[5 - 1]+ flist[5 - 2])
s = len(flist)
print(s)
print(flist[s-1])'''