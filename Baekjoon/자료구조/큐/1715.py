# deque로 풀려고 했는데 시간 초과로 불가능함
# 우선 순위 큐인 heapq를 이용해서 풀어야 정답 도출 가능
# 우선 순위 큐 heapq!!!!

# 최대 힙은 튜플을 사용한다
# heap_items = [1,3,5,7,9]

# max_heap = []
# for item in heap_items:
#   heapq.heappush(max_heap, (-item, item))

# max_item = heapq.heappop(max_heap)[1]
# print(max_item)

import heapq
import sys
input = sys.stdin.readline

N = int(input())
cards = []
for _ in range(N):
    cards.append(int(input()))

heapq.heapify(cards) # heapify: heap구조로 변환

ans = 0
# len(cards) > 1 인 이유는
# 두 카드를 더해야 하기 때문이다.
# len(cards) == 1 이면 sum_value의 마지막 값이 들어가있는 상태이므로 의미 없음
while len(cards) > 1:
    first_card = heapq.heappop(cards) # 가장 작은거 꺼내오기
    second_card = heapq.heappop(cards) # 가장 작은거 꺼내오기
    sum_value = first_card + second_card
    ans += sum_value
    heapq.heappush(cards, sum_value) # 다시 넣기

print(ans)