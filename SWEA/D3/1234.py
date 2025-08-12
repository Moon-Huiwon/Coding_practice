#%%
# stack 활용한 코드
for t in range(10):
    N, tmp_password = map(str, input().split())
    stack = []
    for num in tmp_password:
        if len(stack) > 0 and stack[-1] == num:
            stack.pop()
        else:
            stack.append(num)
    print(f'#{t+1} {"".join(stack)}')

#%%
# stack 활용 안한 코드
def password_seperate(n):

    if n == 0:
        return []
    else:
        return password_seperate(n // 10) + [n%10]
    
        
def delete(password, idx, N):

    if idx >= N - 1:
        return int(''.join(map(str, password)))

    if (password[idx] == password[idx+1]):
        
        change_password_list = list(password[:idx]) + list(password[idx+2:])
        
        return delete(change_password_list, 0, len(change_password_list))
    
    else:
        
        return delete(password, idx + 1, len(password))


for t in range(10):
    N,  tmp_password = map(int, input().split())

    password_list = password_seperate(tmp_password)

    real_password = delete(password_list, 0, N)

    print(f'#{t+1} {real_password}')


