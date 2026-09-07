s = input()

max_len = 1
curr_len = 1

i = 1
while i < len(s):
    if s[i] == s[i - 1]:
        curr_len = curr_len + 1
        if curr_len > max_len:
            max_len = curr_len
    else:
        curr_len = 1
    i = i + 1

print(max_len)
