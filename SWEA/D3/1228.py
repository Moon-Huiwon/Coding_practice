#%%
def find_code(code, command):
    if len(command) > 0:
        x = int(command[1])
        y = int(command[2])
        change_code = code[:x] + command[3 : 3 + y] + code[x:]
        change_command = command[y+3:]
        return find_code(change_code, change_command)
    else:
        print(f'#{t+1} {" ".join(map(str, code[:10]))}')
        
for t in range(10):
    N = int(input())

    code = list(map(int, input().split()))
    command_cnt = int(input())
    command = list(map(str, input().split()))

    find_code(code, command)



#%%

for t in range(10):
    N = int(input())
    code = list(map(int, input().split()))
    command_cnt = int(input())
    command = list(map(str, input().split()))

    while len(command) > 0:
        x = int(command[1])
        y = int(command[2])
        code = code[:x] + command[3 : 3 + y] + code[x:]
        command = command[y+3:]


    print(f'#{t+1} {" ".join(map(str, code[:10]))}')


