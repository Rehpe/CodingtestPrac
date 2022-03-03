#dfs/ bfs - 단지 번호 붙이기
#백준 https://www.acmicpc.net/problem/2667 난이도

'''
1. N X N 크기의 지도
2. 1은 집이 있는곳, 0은 집이 없는 곳
3. 단지수를 출력하고, 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력

입력
1. N 입력
2. N개만큼의 지도정보
출력
단지수, 단지수 n개 만큼의 집 총 수를 오름차순으로
'''


n = int(input())
graph = []
houselist =[]
house = 0


for _ in range(n):
    graph.append(list(map(int, input())))

#상하좌우 탐색
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y):
    global house
    if x<=-1 or y<=-1 or x>=n or y>=n:
        return False    
    if graph[x][y] == 0:
        return False
    if graph[x][y] == 1:
        house += 1
        graph[x][y] = 0
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False

result = 0

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            dfs(i,j)
            houselist.append(house)
            result +=1
            house = 0

houselist.sort()
print(result)
for i in range(result):
    print(houselist[i])
