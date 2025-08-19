def find_card(num_card):

    if len(num_card) == 1:
        return num_card[0]

    # 문제 조건 잘 볼것...
    # 홀수를 2개의 그룹으로 나눌때 왼쪽에 더 많게 그룹 생성
    # ex) [3, 2]
    # 간단한 mid 구하는 식: mid = (len(num_card) - 1) // 2 + 1 
    if len(num_card) % 2 == 0:
        mid = len(num_card) // 2
    else:
        mid = len(num_card) // 2 + 1

    # 두 학생의 카드 확인 (카드가 1개가 될때까지 쪼개진다)
    student1 = find_card(num_card[:mid])
    student2 = find_card(num_card[mid:])
    
    # student2가 이기면 student2 출력
    # 그렇지 않으면 student1 출력 (무승부일때 가능한 이유는 student1이 index가 더 작기 때문)
    if student1[1] == 1:
        if student2[1] == 2:
            return student2
        else:
            return student1
    elif student1[1] == 2:
        if student2[1] == 3:
            return student2
        else:
            return student1
    elif student1[1] == 3:
        if student2[1] == 1:
            return student2
        else:
            return student1

T = int(input())
for t in range(T):
    N = int(input())
    cards = list(map(int, input().split()))
    num_card = []
    for i in range(N):
        num_card.append([i+1, cards[i]])

    ans = find_card(num_card)
    print(f'#{t+1} {ans[0]}')
