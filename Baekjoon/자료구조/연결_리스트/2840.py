# 우리는 시계 반대 방향으로 데이터를 입력하고 있으므로
# 출력할 때는 시계 방향으로 출력해야 한다는 점을 유의***
# 중복 알파벳이 작성되면 안되는 조건 까먹지 말것!
import sys
input = sys.stdin.readline

from collections import deque

N, K = map(int, input().rstrip().split())
paper = deque(['?'] * N)

check = True
for _ in range(K):
    num, word = map(str, input().rstrip().split())
    paper.rotate(-int(num))
    if paper[0] != '?' and paper[0] == word:
        continue
    elif paper[0] != '?' and paper[0] != word:
        check = False
        break
    elif paper[0] != word and word in paper:
        check = False
        break
    
    paper[0] = word

if check:
    paper.rotate(-1)
    for i in range(N-1, -1, -1):
        print(paper[i], end="")
else:
    print('!')
