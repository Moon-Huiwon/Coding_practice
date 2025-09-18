# math 함수 사용
import sys
input = sys.stdin.readline

import math
N = int(input())
rings = list(map(int, input().split()))

for i in range(1,N):
    gcd_value = math.gcd(rings[0], rings[i])
    print(f'{rings[0]//gcd_value}/{rings[i]//gcd_value}')


#%%
# 함수 사용X
N = int(input())
rings = list(map(int, input().split()))

for i in range(1,N):
    if rings[0] % rings[i] == 0:
        print(f'{rings[0]//rings[i]}/{1}')
    else:
        max_num = 1
        num = 1
        while min(rings[0], rings[i]) >= num:
            if rings[0] % num == 0 and rings[i] % num == 0:
                max_num = num
            num += 1
        
        print(f'{rings[0]//max_num}/{rings[i]//max_num}')

#%%
# 최대공약수 함수 설정
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

N = int(input())  # 링의 개수
rings = list(map(int, input().split()))  # 링들의 크기

# 첫 번째 링을 기준으로 나머지 링들의 비율을 계산
for i in range(1, N):
    gcd_value = gcd(rings[0], rings[i])  # 최대 공약수 계산
    print(f'{rings[0] // gcd_value}/{rings[i] // gcd_value}')  # 약분된 분수 출력