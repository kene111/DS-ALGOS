# This code runs perfectly when the values in the arrays are little.
arr = [1, 5, 3]
set_a = [3, 1]
set_b = [5, 7]

new_set_a = []
new_set_b = []
m = 0
n = 0

for k in set_b:
    for p in arr:
        if k == p:
            new_set_b.append(k)

for q in set_a:
    for o in arr:
        if q == o:
            new_set_a.append(q)


for t in new_set_b:
    m += 1

for T in new_set_a:
    n += 1

b = n - m
print(b)




# Using Sets ..................................................
""" arr = {1, 5, 3}
set_a = {3, 1}
set_b = {5, 7}

new_set_a = set()
new_set_b = set()
m = 0
n = 0

for k in set_b:
    for p in arr:
        if k == p:
            new_set_b.add(k)

for q in set_a:
    for o in arr:
        if q == o:
            new_set_a.add(q)


for t in new_set_b:
    m += 1

for T in new_set_a:
    n += 1

b = n - m
print(b)
 
 """

# Another way ...................
""" n = 0
m = 0
arr = {1, 5, 3}
set_a = {3, 1}
set_b = {5, 7}

v_a = set_a & arr  # Shows values that are identical in both sets
v_b = set_b & arr  # Shows values that are identical in both sets




n = len(v_a)
m = len(v_b)
b = n-m
print(n-m)

 """

""" for i in arr:
    if i in v_a:
        n += 1

    if i in v_b:
        m += 1 
 """
arr = [1, 5, 3]
set_a = [3, 1]
set_b = [5, 7]

new_set_a = []
new_set_b = []
m = 0
n = 0

for k in set_b:
    for p in arr:
        if k == p:
            new_set_b.append(k)

for q in set_a:
    for o in arr:
        if q == o:
            new_set_a.append(q)


n = len(new_set_a)
m = len(new_set_b)


b = n - m
print(b)