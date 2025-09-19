def recursion(l, r):
    global cnt
    
    if l >= r:
        return 1
    elif s[l] != s[r]:
        return 0
    else:
        cnt += 1
        return recursion(l+1, r-1)

T = int(input())
for _ in range(T):
    s = input()
    cnt = 1
    print(recursion(0, len(s)-1), cnt)