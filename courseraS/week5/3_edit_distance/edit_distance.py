# Uses python3
def edit_distance(s, t):
    #write your code here
    len_s =  len(s)
    len_t = len(t)

    # so many issues occured while trying to use a list, i.e out of range issues.

    #backtrack = [[0 for x in range(len_s+1)] for x in range(len_t+1)]
    backtrack = {}

    for i in range(len_s+1):
        backtrack[i,0] = i

    for j in range(len_t+1):
            backtrack[0,j] = j
    
    for i in range(1,len_s+1):
        for j in range(1,len_t+1):

            insertion =backtrack[i, j-1] + 1       # backtrack[i][j-1] + 1
            deletion = backtrack[i-1, j] + 1       # backtrack[i-1][j] + 1
            match = backtrack[i-1, j-1]            # backtrack[i-1][j-1]
            mismatch = backtrack[i-1, j-1] + 1     # backtrack[i-1][j-1] + 1


            if s[i-1] == t[j-1]:
                backtrack[i,j] = min(insertion,deletion,match)

            else:
                backtrack[i,j] =  min(insertion,deletion,mismatch)

    
    return backtrack[len_s, len_t]
    

if __name__ == "__main__":
    print(edit_distance(input(), input()))
