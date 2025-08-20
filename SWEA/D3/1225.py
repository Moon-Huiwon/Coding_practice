#%%
# 슬라이싱 활용 코드
for _ in range(10):

    t = int(input())
    password_arr = list(map(int, input().split()))

    diff_num = 1

    while diff_num > 0:
        for i in range(1, 6):
            
            if diff_num <= 0:
                break
            
            diff_num = password_arr[0] - i
            if diff_num > 0: 
                password_arr = password_arr[1:] + [diff_num]
            else:
                password_arr = password_arr[1:] + [0]

    print(f'#{t} {" ".join(map(str, password_arr))}')

# %%
# pop() 활용 코드 -> 조금 더 빠름
for _ in range(10):

    t = int(input())
    password_arr = list(map(int, input().split()))

    flag = True
    while flag:
        for i in range(1, 6):

            password = password_arr.pop(0) - i
            if password > 0:
                password_arr.append(password)
            else:
                password_arr.append(0)
                flag = False
                break

    print(f'#{t} {" ".join(map(str, password_arr))}')