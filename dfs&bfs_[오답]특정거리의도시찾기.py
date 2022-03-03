#dfs/ bfs - 특정 거리의 도시 찾기
#백준 https://www.acmicpc.net/problem/18352 난이도 1.5

'''
1.1번부터 N번까지의 도시와 M개의 단방향 도로
2.모든 도로 거리는 1
3.특정 도시 X로부터 출발하여 도달할 수 있는 모든 도시 중 최단거리가 정확히 K인 모든 도시
번호 출력하기. (단 X부터 X 거리는 0)


입력
1. 도시갯수 N, 도로 개수 M, 거리 정보 K, 출발 도시 번호 X 입력
2. M개 줄만큼 자연수 A, B가 공백으로 주어짐 (A번 도시에서 B번 도시로 이동하는 단방향 도로)
출력
1. X로 출발할 수 있는 도시 중 최단거리가 K인 도시 번호를 오름차순으로 한줄에 하나씩
2. 존재하지 않으면 -1 출력
'''
from collections import deque

n, m, k, x = map(int, input().split())

roads= [[] for _ in range(n+1)] #0인덱스를 비우기 위해 n+1개 생성

for _ in range(m):
    a, b = map(int, input().split())
    roads[a].append(b)

distance = [-1] * (n+1) #거리 리스트 하나 만들고 -1로 초기화(0인덱스를 비우기 위해 n+1개 생성)
distance[x] = 0

queue = deque()
queue.append(x)

while queue:
    now = queue.popleft() #큐 뽑은 번호 도시에서 갈 수 있는 곳 검색
    for next_city in roads[now]:
        # 아직 방문하지 않은 도시라면
        if distance[next_city] == -1: 
            distance[next_city] = distance[now] + 1
            queue.append(next_city)

check = False
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)
