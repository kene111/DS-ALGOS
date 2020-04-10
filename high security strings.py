string_ = 'gosafe'
weight_a = 5

dictionary = {"a": 0,
              'b':0,
              'c':0,
              'd': 0,
              'e': 0,
              'f': 0,
              'g':0,
              'h':0,
              'i':0,
              'j':0,
              'k':0,
              'l':0,
              'm':0,
              'n':0,
              'o':0,
              'p':0,
              'q':0,
              'r':0,
              's':0,
              't':0,
              'u':0,
              'v':0,
              'w':0,
              'x':0,
              'y':0,
              'z':0
              }
for key in dictionary:
    dictionary[key] = weight_a
    weight_a += 1
    if dictionary[key] == 25:
        weight_a -= 26

print(dictionary)

score = 0
for i in string_:
    score += dictionary[i]

print(score)