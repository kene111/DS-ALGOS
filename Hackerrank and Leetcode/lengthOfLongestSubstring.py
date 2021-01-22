s="abcabcbb"
ss="bbbbb"
sss="pwwkew"
s0=""

# Works for the cases above but crashes on others
def lengthOfLongestSubstring(s):
    if s == "" or s == " ":
        return len(s)

    hold_position = dict()
    hold_max_score = []

    for i in range(len(s)):
        if s[i] in hold_position:
            hold_max_score.append(len(s[hold_position[s[i]]:i]))
            hold_position[s[i]] = i
        else:
            hold_position[s[i]] = i
            
    return(max(hold_max_score))


    

def lengthOfLongestSubstring2(s):
    
    hold_position = dict()
    max_length = 0
    start_point = 0

    for i in range(len(s)):
        if s[i] in hold_position and start_point <= hold_position[s[i]]:
            
            start_point = hold_position[s[i]] + 1
            
        else:
            
            max_length = max(max_length, i - start_point + 1)
            
        hold_position[s[i]] = i
            
    return(max_length)

# reference --> https://www.youtube.com/watch?v=focOe_mJ7NY


        



print(lengthOfLongestSubstring(sss))