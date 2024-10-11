import heapq

q = int(input())
orders = list()
for i in range(q):
    orders.append(list(map(int,input().split())))

graph = list() #graph[u] = [v, w]
trip_dict = dict() #['id' : [revenue, dest]]
cur_source = 0 #출발지
cost_matrix = list()
# cost_table = list() #cost_table[v] = v까지 도달하는 최적 cost
#----
def calculate(source): #dijkstra!!!
    global graph
    cost_table = [-1 for i in range(len(graph))]
    visited = [False for i in range(len(graph))]
    hq = list() #최소힙
    heapq.heappush(hq, (0,source)) 
    cost_table[source] = 0
    while(len(hq)>0):
        node = heapq.heappop(hq)[1]
        visited[node] = True
        for adj_node, adj_cost in graph[node]:
            if not visited[adj_node]:
                cost_table[adj_node] = min(cost_table[node]+adj_cost, cost_table[adj_node] if cost_table[adj_node] >= 0 else cost_table[node]+adj_cost+10)
                heapq.heappush(hq, (cost_table[adj_node], adj_node))
    return cost_table

def build(order):
    global graph, cost_matrix
    n,m = order[1], order[2]
    graph = [[]for i in range(n)]
    cost_matrix = [[] for i in range(n)]
    idx = 3
    while (idx < len(order)):
        v,u,w = order[idx], order[idx+1], order[idx+2]
        graph[v].append([u,w])
        graph[u].append([v,w])
        idx+=3
    for i in range(n):
        cost_matrix[i] = calculate(i) #cost table update

def generate(order):
    global trip_dict
    trip_dict[order[1]] = order[2:]

def cancel(order):
    if order[1] in trip_dict:
        del trip_dict[order[1]]
    return 1

def sell(order):
    global graph, trip_dict, cur_source, cost_matrix
    cost_table = cost_matrix[cur_source]
    #trip_dict -> ['id' : [revenue, dest]]
    trips = list(filter(lambda x: 0<=cost_table[trip_dict[x][1]]<=trip_dict[x][0], trip_dict.keys()))
    trips.sort(key=lambda x: (-(trip_dict[x][0]-cost_table[trip_dict[x][1]]), x))
    if len(trips) > 0:
        print(trips[0])
        del trip_dict[trips[0]]
    else:
        print(-1)

def update(order):
    global cur_source
    cur_source = order[1]

def stage(order):
    if order[0]==100:
        build(order)
    elif order[0]==200:
        generate(order)
    elif order[0]==300:
        cancel(order)
    elif order[0]==400:
        sell(order)
    else:
        update(order)
#---
for order in orders:
    stage(order)