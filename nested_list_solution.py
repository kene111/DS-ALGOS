n = int(input('put in the number of student'))
my_list = []
new_list = []

for _ in range(n):
    name = input('name?')
    score = float(input('grade score?'))
    my_list.append([name, score])

print(my_list)
min_num = min(my_list, key=lambda x: x[1])

for scores in my_list:
    if scores == min_num:
        my_list.remove(min_num)

print(my_list)

min_num = min(my_list, key=lambda x: x[1])[1]
print(min_num)

for scores in my_list:
    if scores[1] == min_num:
        new_list.append(scores[0])

print(new_list)

#or ...........................................................................................................................................................

n = int(input('put in the number of student'))
my_list = []
new = []
renew = []
for _ in range(n):
    name = input('name?')
    score = float(input('grade score?'))
    my_list.append([name, score])

print(my_list)

for mist in my_list:
    new.append(mist[1])

sort_new = sorted(set(new))
sec_low_grade = sort_new[1]

for mist in my_list:
    if mist[1] == sec_low_grade:
        renew.append(mist[0])

sort_renew = sorted(renew)

for name in sort_renew:
    print(name)


resorted_work = sorted(new_list)

for name in resorted_work:
    print(name) 