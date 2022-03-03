#dfs/ bfs - 연구소
#백준 https://www.acmicpc.net/problem/14502 난이도 2

'''
1.N x M 크기의 연구소
2. 0은 빈 칸, 1은 벽, 2는 바이러스
3. 바이러스는 인접한 상하좌우 빈칸으로 퍼져나갈 수 있다
4. 세울 수 있는 벽의 개수는 3개이며 꼭 3개를 다 세워야 함
5. 벽 3개를 세우고, 바이러스가 다 퍼진 후에 퍼지지 않은 안전영역(0) 크기의 최댓값 구하기


입력
1. 세로 크기 N, 가로 크기 M
2. N개의 연구소 지도 주어짐 (2<= 2(바이러스)의 갯수 <=10)
3. 빈칸의 갯수는 3개 이상
출력
1. 얻을 수 있는 안전 영역의 최대 크기
'''


#전 연구소를 다 순회해야하므로 bfs를 사용해보자

from collections import deque

n, m = map(int, input().split())
lab = []

for _ in range(n):
    lab.append(list(map(int,input().split())))

