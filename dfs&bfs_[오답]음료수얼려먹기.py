#dfs/ bfs - 음료수 얼려먹기
#실전3 (page 149) 난이도 1.5

#N X M 크기의 얼음판
#0은 빈칸, 1은 칸막이
#0이 상하좌우 붙어있으면 한 개로 연결되어있는 것으로 가정
#얼음틀 모양이 주어졌을 때 생기는 얼음 갯수를 구하라


#입력
# N, M이 공백으로 주어짐
# 이후 N번만큼 얼음 틀의 형태가 주어짐(공백 없이)
#출력
# 생기는 얼음의 갯수
from collections import deque

n, m = map(int, input().split())
icemap = []

for _ in range(n):
    icemap.append(list(map(int, input())))

def dfs(x,y):
    #자 이제 첫번째부터 dfs를 돌리겠습니다
    #우선 N X M 범위를 벗어나면 안되니까 이 경우에는 모조리 종료
    if x<=-1 or y<=-1 or x>=n or y >=m:
        return False
    #현재 노드(좌표)를 아직 방문하지 않았다면 / 칸막이가 아니라면
    if icemap[x][y] ==0:
        #해당 좌표 방문처리
        icemap[x][y] = 1
        #그 좌표의 상,하,좌,우 상황도 판별해본다(재귀함수!!)
        dfs(x-1,y) #상
        dfs(x,y-1) #좌
        dfs(x+1,y) #하
        dfs(x,y+1) #우
        return True #네방향 탐색이 다 끝나고 탐색할 것이 더 없다면 true
    return False


dfsresult = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            dfsresult += 1
    

#이동 방향 정의 (상-하-좌-우 순)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
        queue = deque()
        queue.append((x,y))
        icemap[x][y] = 1

        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx >=n or ny>=m or nx<=-1 or ny<=-1:
                    continue
                if icemap[nx][ny] ==1:
                    continue
                if icemap[nx][ny] ==0:
                    queue.append((nx,ny))
                    icemap[nx][ny] =1


bfsresult = 0
for a in range(n):
    for b in range(m):
        if icemap[a][b] ==0:
            bfs(a,b)
            bfsresult+=1        
      

# print(dfsresult)
print(bfsresult)


#37항 True가 어떻게 한 덩어리당 한번만 호출이 될 수 있는지 아직 이해가 부족함
#재귀함수가 값을 반환하는 것에 대한 질문
#재귀함수가 끝나면 보통 값을 반환하지 않음
#값을 반환하는 경우에는 값을 쌓거나 결과값을 가지고 계산을 해야하는 경우
#
#왜 visited[] 리스트를 따로 만들지 않고 주어진 그래프 자체를 덮어씌우는가? 괜찮은건가?
#방문 후 원본 그래프를 변화시키지 않고 탐색해야하는 경우 visited[]가 필요하다
#원본 그래프에 변화를 줌에도 불구하고 중복 탐색할 여지가 있을 경우에도 visited[]가 필요

