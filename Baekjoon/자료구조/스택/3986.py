# import sys
# input = sys.stdin.readline
# 위의 구문 쓸 경우 list(input().rstrip()) 활용해야함
N = int(input())
best_word_cnt = 0
for num in range(N):
    word = list(input())

    if word.count('A') % 2 > 0 or word.count('B') % 2 > 0:
        continue
    
    stack = []
    for w in word:
        
        if len(stack) > 0 and stack[-1] == w:
            stack.pop()
        else:
            stack.append(w)
    
    if len(stack) == 0:
        best_word_cnt += 1

print(best_word_cnt)
