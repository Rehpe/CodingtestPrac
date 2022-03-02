from collections import deque

def dfs(graph, v, visited):
    #현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    #현재 노드와 연결된 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


def bfs(graph,start,visited):
    #Que 구현을 위해 deque 라이브러리 사용
    queue = deque([start]) #deque는 그냥 que기능을 가진 1차원 list라고 생각하자 즉 list([1])
    #현재 노드를 방문 처리
    visited[start] = True
    #큐가 빌 때까지 반복
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7],
]

visited_dfs = [False] * 9
visited_bfs = [False] * 9

print(dfs(graph,1,visited_dfs))
print(bfs(graph,1,visited_bfs))
