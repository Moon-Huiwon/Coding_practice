def gcd(a,b):
    while b:
        a, b = b, a%b
    
    return a

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    num = gcd(a, b)
    tmp_b = b//num
    print(a*tmp_b)