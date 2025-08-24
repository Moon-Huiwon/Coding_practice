import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt")

from collections import deque


T = int(input())
for _ in range(T):
    reverse_cnt = 0 # reverse 할건지 확인하기 위해
    possible = True 
    p = input().strip()
    n = int(input())
    x = input().strip()
    x = x[1:-1] # 괄호 없애기***
    if x == '':
        x = deque() # n==0이면 deque()로 재정의 (안그러면 deque(['']))으로 생성됨
    else:
        x = deque(x.split(',')) # 아니면 ,를 기준으로 나눠주기
    
    for cmd in p:
        if cmd == 'R':
            reverse_cnt += 1 # reverse 횟수 카운트
        else:
            if len(x) > 0:
                if reverse_cnt % 2 == 0: # reverse가 안되면 앞에 숫자 제거
                    x.popleft()
                else:
                    x.pop() # reverse 되었다면 뒤에 숫자 제거
            else:
                print('error') # 제거할 숫자가 없으면 error
                possible  = False
                break
    
    if possible: # error가 안났으면 출력
        if reverse_cnt % 2 != 0: # reverse 해야하면 reverse 진행
            x.reverse()
        print('[' + ','.join(x) + ']') # 출력하기


