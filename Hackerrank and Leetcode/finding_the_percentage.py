n = int(input())
student_marks = {}

for _ in range(n):
    line = input().split()
    scores = list(map(float, *line))
    student_marks[line[0]] = scores

query_name = input()

yeah = sum(student_marks[query_name])
finals = yeah/len(query_name)

print("{:.2f}".format(finals))