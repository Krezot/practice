N = int(input())
u = list(map(int, input().split()))
l_element = 0
while l_element < N - 1 and u[l_element] <= u[l_element + 1]:
    l_element += 1
if l_element == N - 1:
    print(0)
else:
    r_element = N - 1
    while r_element > 0 and u[r_element - 1] <= u[r_element]:
        r_element -= 1
    result = min(N - (l_element + 1), r_element)
    i, j = 0, r_element
    while i < l_element and j < N:
        if u[i] <= u[j]:
            result = min(result, j - i - 1)
            i += 1
        else:
            j += 1
    result = min(result, j - i - 1)
    print(result)
