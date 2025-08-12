import sys
input = sys.stdin.readline

# VPS_Check를 활용해서 코드 구성
T = int(input())
for _ in range(T):
    VPS_check = 0
    PS = list(input().strip())
    
    if PS[0] == '(':
        for s in PS:
            if s == '(':
                VPS_check += 1
            else:
                VPS_check -= 1

            if VPS_check < 0:
                print('NO')
                break

        if VPS_check == 0:
            print('YES')
        elif VPS_check > 0:
            print('NO')
    else:
        print('NO')

# replace() 함수 활용하여 코드 작성
import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    temp = input().rstrip()
    while True:
        if '()' in temp:
            temp = temp.replace('()','')
        else:
            if len(temp) == 0:
                print('YES')
            else:
                print('NO')   
            break