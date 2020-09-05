k = [2,3,4,5,6]
#i=0
hold = list()
#print(k[i+2])

p = 0
v =  2

for i in range(len(k)):
    for j in range(len(k)):
        if p == 0:
            hold.append(k[i]+k[j+v])
            p += 1
        if p >= 1 :
            v = 1
            hold.append(k[i]+k[j+v])

        if j == len(k)-1:
            p = 0
            v = 2
        print(hold)
print(max(hold))
