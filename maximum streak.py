toss = ['Tails', 'Tails', 'Tails','Heads', 'Tails', 'Tails', 'Heads', 'Tails', 'Heads', 'Heads']
head_position = []
tail_position = []

for i in range(len(toss)):
    if toss[i] == 'Heads':
        head_position.append(i)
    else:
        tail_position.append(i)

head_count = 0
for i in range(len(head_position)-1):
    if head_position[i+1] - head_position[i] == 1:
        head_count += 1

print('This is the head_position', head_position)
print('This is the tail_position', tail_position)
print('The head count is ', head_count)
tail_count = 0
for i in range(len(tail_position)-1):
    if tail_position[i+1] - tail_position[i] == 1:
        tail_count += 1



print('The tail count is ',tail_count)
if tail_count == 0:
    tail_count = 0
else:
        tail_count += 1


if head_count == 0:
    head_count = 0
else:
    head_count += 1

print('Final head count is',head_count)
print('Final tail count is',tail_count)



