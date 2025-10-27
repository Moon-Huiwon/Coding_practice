def backtracking(tmp_password):
    if len(tmp_password) == L:
        cnt = 0
        for string in ['a', 'e', 'i', 'o', 'u']:
            if tmp_password.count(string) > 0:
                cnt += tmp_password.count(string)
        if 0 < cnt <= L-2:
            print(''.join(tmp_password))
    
    for i in range(C):
        if visited[i] == 0 and (len(tmp_password) == 0 or ord(tmp_password[-1]) < ord(alphabet[i])) :
            visited[i] = 1
            backtracking(tmp_password + [alphabet[i]])
            visited[i] = 0

L, C = map(int, input().split())
alphabet = list(input().split())
alphabet.sort()
visited = [0]*C
backtracking([])