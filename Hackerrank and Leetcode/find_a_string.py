def count_substring(s, s_s, v=0):
    for i in range(len(s)):
        if s[i:i+len(s_s)] == s_s:
            v += 1

    return v


string = input('main').strip()
sub_string = input('sub main').strip()

count = count_substring(string, sub_string)

print(count)






