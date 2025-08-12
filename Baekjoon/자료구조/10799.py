stick_laser = input()
stick_laser = stick_laser.replace('()', 'L')
stack = []
cnt = 0
for s in stick_laser:
    if s == '(':
        stack.append('(')
    elif s == 'L':
        cnt += len(stack)
    else:
        if len(stack) > 0 and stack[-1] == '(':
            stack.pop()
            cnt += 1
print(cnt)

#%%
# 다른 코드
stick_laser = list(input())
stack = []
piece_cnt = 0
for i in range(len(stick_laser)):
    if stick_laser[i] == '(':
        stack.append(stick_laser[i])
    else:
        if stick_laser[i-1] == '(':
            stack.pop()
            piece_cnt += len(stack)
        else:
            stack.pop()
            piece_cnt += 1

print(piece_cnt)

