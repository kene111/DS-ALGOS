# Uses python3
import sys

def optimal_sequence_0(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
            
        else:
            n = n - 1
    return reversed(sequence)

def optimal_sequence_1(n):
    sequence = []
    m = n + 1
    backtrack = [0] * m
    backtrack[1] = 0
    


    for i in range(2, m):

        val1,val2,val3 = m,m,m
        
        if i%2 == 0:
            val2 =  backtrack[i//2] + 1
        if i%3 == 0:
            val3=  backtrack[i//3] + 1
        else:
            val1 = backtrack[i - 1] + 1
        
        backtrack[i] = min(val1,val2,val3)

    #print(backtrack)
    sequence.append(n)

    while  n!=1:
        if n % 2 == 0 and backtrack[n//2]+1 <= backtrack[n]:
            n = n //2
            sequence.append(n)

        if n % 3 == 0 and backtrack[n//3]+1 <= backtrack[n]:
            n = n //3
            sequence.append(n)

        if  backtrack[n-1]+1  <= backtrack[n] :
            n = n -1
            sequence.append(n)
    
    return reversed(sequence)


#input = sys.stdin.read()
n = int(input())
sequence = list(optimal_sequence_1(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')


# https://www.coursera.org/learn/algorithmic-toolbox/discussions/weeks/5/threads/d8xwlPCNEeWkUAr_DMJ5Lw