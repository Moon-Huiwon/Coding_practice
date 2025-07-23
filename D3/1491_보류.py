#%%
import math
T = int(input())
for t in range(T):
    N, A, B = map(int, input().split())

    answer_list = []

    R = int(math.sqrt(N))
    C = int(math.sqrt(N))
    value = A*abs(R-C) + B*(N - R*C)
    answer_list.append(value)

    tmp = int(math.sqrt(N))
    while N % tmp == 0:
        tmp += 1
    R = tmp
    C = int(N // tmp)
    value = A*abs(R-C) + B*(N - R*C)
    answer_list.append(value)

    print(f'#{t+1} {min(answer_list)}')
            


# %%
import math

N, A, B = map(int, input().split())

answer_list = []

R = int(math.sqrt(N))
C = int(math.sqrt(N))
value = A*abs(R-C) + B*(N - R*C)
answer_list.append(value)

tmp = int(math.sqrt(N))
while N % tmp == 0:
    tmp += 1
R = tmp
C = int(N // tmp)
value = A*abs(R-C) + B*(N - R*C)
answer_list.append(value)

print(f'#{t+1} {min(answer_list)}')
            
