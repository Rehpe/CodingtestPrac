#dfs/ bfs - 미로 탈출
#실전4 (page 152) 난이도 1.5

'''
1. N X M 크기의 미로
2. 동빈이의 위치는 (1,1), 출구의 위치는 (N,M)
3. 괴물이 있는 곳은 0, 없는 곳은 1
4. 괴물을 피해 탈출할 수 있는 최소 칸의 개수 구하기


입력
1. N, M이 공백을 두고 입력
2. M개 만큼의 미로정보
출력
시작 위치에서 N,M까지 괴물을 피해 탈출하는 최소 칸의 개수
'''

from collections import deque

n, m = map(int, input().split())
maze =[]

for _ in range(m):
    maze.append(list(map(int, input())))

#이동 방향 정의 (상-하-좌-우 순)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append(x,y)

    while queue:
        x, y =queue.popleft()
        for i in range(4):
            nx = x +dx[i]
            ny = y +dy[i]

            if nx <0 or ny<0 or nx>=n or ny>=m:
                continue
            if maze[nx][ny] ==0:
                continue
            if maze[nx][ny] ==1:
                maze[nx][ny] = maze[x][y]+1
                queue.append(nx,ny)

    return maze[n-1][m-1]


print(bfs(0,0))
