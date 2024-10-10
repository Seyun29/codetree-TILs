n = int(input())
jobs = list()
# visited = [False for i in range(n)]
for i in range(n):
    jobs.append(list(map(int,input().split())))
# jobs.sort(key=lambda x:x[0])

total_cost = 0
#-------
def dfs(idx, end_time, cost):
    global total_cost
    # print(idx, end_time, cost)
    if idx >= n-1:
        if end_time <= idx:
            cost += jobs[idx][1]
        total_cost = max(total_cost, cost)
        return
    if end_time <= idx:
        dfs(idx+1, idx+jobs[idx][0], cost+jobs[idx][1])
    dfs(idx+1, end_time, cost)

dfs(0,0,0)
print(total_cost)