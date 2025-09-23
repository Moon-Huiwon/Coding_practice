def gcd(a,b):
    while b:
        a, b = b, a%b
    return a


first_A, first_B = map(int, input().split())
second_A, second_B = map(int, input().split())

A = first_A*second_B + second_A*first_B
B = first_B*second_B

num = gcd(A, B)

print(f'{A//num} {B//num}')
