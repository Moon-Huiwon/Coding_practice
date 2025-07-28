# %%
import math


def process(N, A, B, R, C):
    return A*abs(R-C) + B*(N-R*C)


T = int(input())
t = 0
for t in range(T):
    
    N, A, B = map(int, input().split())
    
    answer = float('inf')
    for num in range(N, 0, -1):
        
        divisors = []
        for i in range(1, int(math.sqrt(num)) + 1):
            if num % i == 0:
                divisors.append(i)
                if i != num // i:
                    divisors.append(num // i)
        
        divisors.sort()

        if len(divisors) % 2 == 0:
            R = divisors[len(divisors) // 2]
            C = divisors[len(divisors) // 2 - 1]
            value = process(N, A, B, R, C)
            if value < answer:
                answer = value
            
        
        else:
            R = divisors[len(divisors) // 2]
            C = divisors[len(divisors) // 2]
            value = process(N, A, B, R, C)
            if value < answer:
                answer = value
        
                
        
    print(f'#{t+1} {answer}')

# %%
# %%
import math


def process(N, A, B, R, C):
    return A*abs(R-C) + B*(N-R*C)

T = int(input())

for t in range(T):
    
    N, A, B = map(int, input().split())
    
    answer = float('inf')
    for num in range(N, 0, -1):
        
        divisors = []
        divisor_num = int(math.sqrt(num))
        
        while len(divisors) == 0:
            if num % divisor_num == 0:
                divisors.append(divisor_num)
                divisors.append(num // divisor_num)
            else:
                divisor_num -= 1
        
        divisors.sort()    
        
        R = divisors[1]
        C = divisors[0]
        value = process(N, A, B, R, C)
        if value < answer:
            answer = value
    
        if answer == 0:
            break
        
    print(f'#{t+1} {answer}')

# %%
