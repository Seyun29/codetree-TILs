from collections import deque
from copy import deepcopy

k,m = list(map(int, input().split()))
piece_map = list()
for i in range(5):
    piece_map.append(list(map(int, input().split())))

wall_q = deque()
for n in list(map(int, input().split())):
    wall_q.append(n)

visited = [[False for i in range(5)]for k in range(5)]

answer = ''
#----
def inRange(y,x):
    if 0<=x<5 and 0<=y<5:
        return True
    else:
        return False

def adjs(y,x):
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]
    ret = list()
    for i in range(4):
        if inRange(y+dy[i], x+dx[i]):
            ret.append([y+dy[i],x+dx[i]])
    return ret

def turn90(input_map, y,x):
    #y,x = center coord // # x,y -> y, -1*x, y,x -> -1*x,y
    #90 degree counterclockwise
    new_map = deepcopy(input_map)
    for r in range(y-1,y+2):
        for c in range(x-1,x+2):
            #0,0 기준 좌표
            o_y, o_x = r-y, c-x
            new_y, new_x = o_x + y, -1*o_y + x
            new_map[new_y][new_x] = input_map[r][c]
    return new_map

def bfs(input_map,r,c): #Spanning Tree Traversal
    if (visited[r][c]):
        return []
    q = deque()
    q.append([r,c])
    visited[r][c] = True
    val = input_map[r][c]
    ret_list = [[r,c]]
    while (len(q)>0):
        node = q.popleft()
        for a_r,a_c in adjs(node[0], node[1]):
            if input_map[a_r][a_c] == val and not visited[a_r][a_c]:
                visited[a_r][a_c] = True
                q.append([a_r,a_c])
                ret_list.append([a_r,a_c])
    return ret_list if len(ret_list) >= 3 else []


def get(input_map):
    global visited
    visited = [[False for i in range(5)]for k in range(5)]
    total_list = []
    for r in range(5):
        for c in range(5):
            total_list += bfs(input_map,r,c)
    return total_list

def put(get_list):
    #get()의 output을 input으로 받음
    get_list.sort(key=lambda e:(e[1], -e[0])) #기준에 따라 sorting
    for r,c in get_list:
        to_add = wall_q.popleft()
        piece_map[r][c] = to_add

def stage():
    # e : [[total_list], 회전한 각도 (1,2,3), 중심좌표[r,c]]
    global piece_map

    stage_list = list()
    for r in range(1,4):
        for c in range(1,4):
            tmp_map = piece_map
            for degree in range(1,4):
                tmp_map = turn90(tmp_map,r,c)
                stage_list.append([get(tmp_map), degree, [r,c]])

    stage_list.sort(key=lambda e:(-len(e[0]),e[1],e[2][1],e[2][0]))

    for i in range(stage_list[0][1]):
        piece_map = turn90(piece_map,stage_list[0][2][0],stage_list[0][2][1])

    put(stage_list[0][0])

    ret_val = len(stage_list[0][0])

    #연쇄 획득 및 put 진행
    further_list = get(piece_map)
    while (len(further_list) > 0):
        # for row in piece_map:
        #     print(row)
        ret_val += len(further_list)
        put(further_list)
        further_list = get(piece_map)
    
    return str(ret_val) if ret_val>0 else False

# ----
for i in range(k):
    stage_res = stage()
    if not stage_res:
        break
    answer += stage_res+' '

print(answer[:-1])