N = int(input())
g = list(map(int, input().split()))


def is_palindrome(num):
    return num == num[::-1]


p = False
if is_palindrome(g):
    p = True
else:
    for i in range(N):
        t = g[:i] + g[i + 1 :]
        if is_palindrome(t):
            p = True
            break
if p == True:
    print("Возможно")
else:
    print("Нет")
