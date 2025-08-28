n = int(input())

f_value = [0]*(n+1)
for n in range(n+1):
    if n <= 1:
        f_value[n] = 1
        f_value[n] = 1
    else:
        f_value[n] = f_value[n-1] + f_value[n-2]*2

print(f_value[n] % 10007)
