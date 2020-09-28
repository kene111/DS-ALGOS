# Uses python3
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def minMax(i,j,m,M,op):
    max_ = -1000000
    min_ =  1000000

    for k in range (i, j):
        a = evalt(M[i][k], M[k+1][j],op[k])
        b = evalt(M[i][k], m[k+1][j],op[k])
        c = evalt(m[i][k], M[k+1][j],op[k])
        d = evalt(m[i][k], m[k+1][j],op[k])
        max_ =   max(max_,a,b,c,d)
        min_ =   min(min_,a,b,c,d)
    
    return(min_,max_)


def get_maximum_value(dataset):
    #write your code here
    op = dataset[1::2]
    d =  dataset[0::2]
    

    n = len(d)

    M = [[0 for _ in range(n)] for _ in range(n)]
    m = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(0,n):
        m[i][i] = int(d[i])
        M[i][i] = int(d[i])



    for s in range(1,n):
        for i in range(0,n-s):

            j = i + s
            m[i][j],M[i][j] = minMax(i,j,m,M,op)

    return M[0][n-1]


if __name__ == "__main__":
    print(get_maximum_value(input()))
