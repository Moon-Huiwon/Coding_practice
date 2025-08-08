# 시간 초과를 해결하기 위한 코드
T = int(input())
for t in range(T):
    # stick과 laser로 구성된 input 받기
    stick_laser = input()
    # laser를 구분하기 위해 'L'로 문자 변경
    stick_laser = list(stick_laser.replace('()', 'L'))

    # 쇠 막대기 별로 laser로 인해 잘라니는 횟수를 확인하기 위해 리스트 생성
    laser_cnt = [0] * stick_laser.count('(')

    # 총 조각의 수를 도출하기 위한 변수 설정
    ans = 0
    # 쇠막대기가 현재 몇개까지 확인되는 지 확인하는 변수(괄호가 열려있는 횟수)
    open_cnt = 0
    for s in stick_laser:
        # 쇠막대기가 시작되면 open_cnt 변수에 +1 (괄호가 열려있는 횟수 카운트) -> 닫히기 전까지 레이저의 영향을 받음
        if s == '(':
            open_cnt += 1
        # 쇠막대기가 존재하고(괄호가 열려있고) laser 위치라면
        # 현재까지 열려있는 쇠막대기 개수의 리스트에 laser 개수 업데이트
        elif open_cnt > 0 and s == 'L':
            for i in range(open_cnt):
                laser_cnt[i] += 1

        # 쇠막대기의 마지막 부분이면 (괄호가 닫히면)
        # 마지막에 저장된 위치의 laser_cnt+1(조각의 수) 값을 ans에 더하기
        # 마지막 부분을 0으로 다시 초기화
        # 쇠막대기가 끝났으므로 (괄호가 닫혔으므로) 존재하는 쇠막대기(괄호가 열려있는)의 수 -1
        elif s == ')':
            ans += laser_cnt[open_cnt - 1] + 1
            laser_cnt[open_cnt - 1] = 0
            open_cnt -= 1

    print(f'#{t + 1} {ans}')

# # 기존 코드 (시간초과)
# # 원인
# # - 가장 위에 있는 막대기를 찾고 이를 지워나가고 다시 그 다음 막대기를 찾는 형식으로 코드 구성
# # - 쇠막대기 하나 지우고 처음부터 다시 찾아나가는 방식으로 인해 시간이 오래 걸림
# T = int(input())
# for t in range(T):
#     # stick과 laser로 구성된 input 받기
#     stick_laser = input()
#
#     # 레이저를 구분하기 위해 '()'를 'L'로 대체
#     stick_laser = list(stick_laser.replace('()', 'L'))
#
#     # 조각의 총 개수 구하기 위한 변수
#     cnt = 0
#     # 출발 지점
#     left = 0
#     # 마지막 지점
#     right = 1
#
#     # stick_laser를 줄여나갈거기 때문에 while문 사용
#     while len(stick_laser) > stick_laser.count('L'):
#
#         # stick_laser에서 선택된 두 구역이 열고 닫혔으면(쇠막대기 확인 가능) 조각 수(laser+1) cnt에 더하기
#         if stick_laser[left] == '(' and stick_laser[right] == ')':
#             cnt += stick_laser[left:right+1].count('L') + 1
#             # 사용된 쇠막대기 제거
#             stick_laser.pop(right)
#             stick_laser.pop(left)
#             # 처음부터 확인하기 위해 초기화
#             left = 0
#             right = 1
#
#         # 쇠막대기 시작점이지만 마지막 지점이 아니고 레이저가 발견된다면 더 오른쪽으로 이동하여 닫힌 곳 찾기
#         elif stick_laser[left] == '(' and stick_laser[right] == 'L':
#             right += 1
#
#         # 위의 내용이 전부 아니면 시작점을 옮겨서 확인
#         else:
#             left += 1
#             right += 1
#
#     print(f'#{t+1} {cnt}')



