row,col,k = list(map(int, input().split()))
#k = 정령수, r행 c열
#map = r+1 * c+1
mapp = [[0 for k in range(col+1)] for i in range(row+1)]
golem_list = list()
for i in range(k):
    tmp = list(map(int, input().split()))
    tmp[0] = [1,tmp[0]]
    tmp.append(2)
    golem_list.append(tmp)
# 0,1,2,3 = 북,동,남,서 -> 동쪽 회전 = (dir+1)%4, 서쪽 회전 = (dir-1)%4
total = 0

def inRange(r,c):
    if 1<=r<=row and 1<=c<=col:
        return True
    else:
        return False

def move(r,c,d, prev, cont):
    global row
    # 정지 조건 (최남단)
    if r>=(row-1):
        return (r,c,d)
    # 남쪽 이동 조건
    if inRange(r+1,c-1) and inRange(r+1,c+1) and inRange(r+2, c) and mapp[r+1][c-1] == 0 and mapp[r+1][c+1] == 0 and mapp[r+2][c] == 0 and mapp[r+1][c] == 0:
        # print('남')
        return move(r+1,c,d,0,0)
    # 서쪽 회전 이동
    elif prev!=1 and inRange(r+1,c-1) and inRange(r,c-2) and inRange(r-1, c-1) and mapp[r+1][c-1] == 0 and mapp[r][c-2] == 0 and mapp[r-1][c-1] == 0:
        # print('서')
        return move(r,c-1,(d-1)%4, 3, cont+1 if prev==3 else 1)
    elif prev==-1 and inRange(r, c-2) and inRange(r+1,c-1) and prev==-1 and mapp[r][c-2] == 0 and mapp[r+1][c-1] == 0:
        # print('서')
        return move(r,c-1,(d-1)%4, 3, 0)
    # 동쪽 회전 이동
    elif prev!=3 and inRange(r,c+2) and inRange(r-1,c+1) and inRange(r+1, c+1) and mapp[r][c+2] == 0 and mapp[r-1][c+1] == 0 and mapp[r+1][c+1] == 0:
        # print('동')
        return move(r,c+1,(d+1)%4, 1, cont+1 if prev==1 else 1)
    elif prev==-1 and inRange(r,c+2) and inRange(r+1,c+1) and prev==-1 and mapp[r][c+2] == 0 and mapp[r+1][c+1] == 0:
        # print('동')
        return move(r,c+1,(d+1)%4, 1, 0)
    else: 
        if prev==3:
            # -서쪽
            # print("-서 *", cont)
            return (r, c+cont, (d+cont)%4)
        elif prev==1:
            # print("-동 *", cont)
            return (r, c-cont, (d-cont)%4)
        return (r,c,d)

def adjacent(r,c, idx):
    ret_list = []
    if inRange(r+1, c) and mapp[r+1][c] != idx and mapp[r+1][c] != 0:
        ret_list.append(mapp[r+1][c]-1)
    elif inRange(r-1, c) and mapp[r-1][c] != idx and mapp[r-1][c] != 0:
        ret_list.append(mapp[r-1][c]-1)
    elif inRange(r, c-1) and mapp[r][c-1] != idx and mapp[r][c-1] != 0:
        ret_list.append(mapp[r][c-1]-1)
    elif inRange(r, c+1) and mapp[r][c+1] != idx and mapp[r][c+1] != 0:
        ret_list.append(mapp[r][c+1]-1)
    return ret_list
    
    

last_idx = 0
for (idx, golem) in enumerate(golem_list):
    # map에 위치시키기
    (o_r, o_c), o_d, l = golem
    r,c,d = move(o_r,o_c,o_d,-1,0)
    mapp[r][c] = idx+1
    if inRange(r+1,c) and inRange(r-1,c) and inRange(r, c+1) and inRange(r, c-1):
        mapp[r+1][c], mapp[r-1][c], mapp[r][c+1], mapp[r][c-1] = idx+1, idx+1, idx+1, idx+1
        d_x, d_y = r-1, c
        if (d==1):
            d_x, d_y = r, c+1
        elif d==2:
            d_x, d_y = r+1, c
        elif d==3:
            d_x, d_y = r, c-1

        adj_list = adjacent(d_x,d_y,idx+1)
        maxx = r+1
        for adj in adj_list:
            maxx = max(golem_list[adj][2], maxx)
        golem_list[idx][2] = maxx

        total+=maxx
        # print('인덱스, 골렘 입력 :', idx+1, o_c, o_d)
        # print('인접리스트 :', adj_list)
        # print('최대값 :', maxx)
        # print('d :', d_x, d_y)
        mapp[d_x][d_y] = 9
        # print("mapp -----")
        # for rows in mapp:
        #     print(rows)
        # print("----\n")
        mapp[d_x][d_y] = idx+1
    else:
        # print('초기화')
        mapp = [[0 for k in range(col+1)] for i in range(row+1)]

 
print(total)