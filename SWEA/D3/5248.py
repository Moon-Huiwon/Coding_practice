import sys
sys.stdin = open('input.txt')

def make_set(N): # 각 집합을 만들어주는 함수
    # 1 ~ n 까지의 원소가 "각자 자기 자신이 대표자라고 설정"
    parents = [i for i in range(N+1)]
    return parents

def find_set(x): # 집합의 대표자를 찾는 함수
    # 자신 == 부모 -> 해당 집합의 대표자
    if x == parents[x]:
        return x
    
    # 경로 압축 코드
    # 내가 대표자를 바로 가리키도록
    parents[x] = find_set(parents[x])

    return parents[x]

def union(x, y): # 두 집합을 합친다.
    # 1. x, y 의 대표자를 검색
    rep_x = find_set(x)
    rep_y = find_set(y)

    # 만약 이미 같은 집합
    if rep_x == rep_y:
        return # 같은 집합끼리는 합칠 필요가 없다
    
    '''
    # 더 작은 쪽으로 연결하는 문제라면, 조건을 추가해준다.
    if rep_x < rep_y:
        parents[rep_y] = rep_x
    else:
        parents[rep_x] = rep_y
    '''

    parents[rep_y] = rep_x

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    parents = make_set(N)
    for i in range(0,len(nums),2):
        union(nums[i], nums[i+1])
    cnt = 0
    for i in range(N+1):
        if parents[i] == i:
            cnt += 1
    print(f'#{t+1} {cnt-1}')