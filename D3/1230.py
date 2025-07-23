#%%
def find_code(code, command):
    if len(command) > 0 and command[0] == 'I':
        x = int(command[1])
        y = int(command[2])
        change_code = code[:x] + command[3 : 3 + y] + code[x:]
        change_command = command[y+3:]
        return find_code(change_code, change_command)
    elif len(command) > 0 and command[0] == 'D':
        x = int(command[1])
        y = int(command[2])
        change_code = code[:x] + code[x+y:]
        change_command = command[3:]
        return find_code(change_code, change_command)
    elif len(command) > 0 and command[0] == 'A':
        y = int(command[1])
        change_code = code + command[2:2+y]
        change_command = command[y+2:]
        return find_code(change_code, change_command)
    else:
        print(f'#{t+1} {" ".join(map(str, code[:10]))}')
        
for t in range(10):
    N = int(input())

    code = list(map(int, input().split()))
    command_cnt = int(input())
    command = list(map(str, input().split()))

    find_code(code, command)