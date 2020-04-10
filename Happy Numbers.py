
def happy_number(x):
    x = str(x)
    t = 0
    for i in x:
        t += (int(i)) ** 2

    if t == 1:
        return True

    elif t == 4:
        return False

    return(happy_number(t))

n = happy_number(200)
print(n)