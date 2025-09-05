# # 시간 초과
# import sys
# # sys.stdin = open("input.txt")
# input = sys.stdin.readline

# max_memory = 100000
# memory = [0] * 100000

# tmp = {}

# N = int(input())
# for _ in range(N):
#     cmd = input().rstrip()
#     if '=' in cmd:
#         cmd = cmd.split('=')
#         var = cmd[0]
#         malloc_num = int(cmd[1][7:-2])

#         zero_start = memory.index(0)
#         if zero_start + malloc_num < max_memory:
#             memory[zero_start:zero_start+malloc_num] = [var]*malloc_num

#             if var not in tmp:
#                 tmp[var] = []
#                 tmp[var].append(zero_start)
#             else:
#                 tmp[var].append(zero_start)

#     elif 'free' in cmd:
#         var = cmd[5:-2]
#         if var in tmp and len(tmp[var]) > 0:
#             var_start = tmp[var].pop()
#             var_cnt = memory[var_start:].count(var)
#             memory[var_start:var_start+var_cnt] = [0]*var_cnt    
    
#     elif 'print' in cmd:
#         var = cmd[6:-2]
#         if var in memory:
#             print(memory.index(var)+1)
#         else:
#             print(0)


