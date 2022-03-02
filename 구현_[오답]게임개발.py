#04. 구현 - 게임 개발
#실전3 (page 118) 난이도 2

# N x M 크기의 맵
# 맵 칸(좌표)는 (A, B) 로 표시
# 캐릭터는 상하좌우 이동 가능, 바다는 갈 수 없다
# 현 위치에서 왼쪽 방향부터 갈 곳을 정함
# 왼쪽 방향에 안 가본 칸이 존재한다면 왼쪽 방향으로 회전 후 한 칸 전진
# 안 가본 칸이 없다면 회전만 함
# 네 방향 모두 갈 수 없는 칸이면 바라보는 방향 유지하고 한 칸 뒤로 간 후에 다시 왼쪽 방향부터 
# 갈 곳 정하기
# 뒤쪽으로도 갈 수 없다면 움직임 종료

#입력
# 공백으로 세로 N, 가로 M 입력
# 캐릭터 좌표 (A, B)와 바라보는 방향 d가 공백으로 입력 (0,1,2,3) ->북,동,남,서
# 세 번째 줄부터 맵 프린트. 맵의 외곽은 항상 바다이다
# 게임 캐릭터가 위치한 곳은 항상 육지이다
#출력
# 캐릭터가 방문한 칸 수 출력


n, m = map(int, input().split())

#방문 위치를 저장하기 위한 맵 생성, 0으로 초기화
d = [[0] * m for _ in range(n)]

x, y, direction = map(int, input().split())
d[x][y] = 1 #현재 좌표 방문처리

#맵 정보 입력받기
map = []
for i in range(n):
    map.append(list(map(int, input().split())))


# 북, 동, 남, 서 정의
dx = [-1,0,1,0 ]
dy= [0,1,0,-1]

# 왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


# 시뮬레이션 시작
count = 1
turn_time =0
while True:
    # 1. 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 2-1.회전 후 정면에 가보지 않은 칸이 있다면 이동
    if d[nx][ny] == 0 and map[nx][ny] == 0: #방문위치 저장맵과 주어진 맵 칸이 둘다 0이면
        d[nx][ny] == 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 2-2. 회전 후 정면이 갔던 칸이나 바다면
    else:
        turn_time += 1
    # 네 방향 모두 갈 수 없는 경우 다시 뒤로 돌아가자
    if turn_time == 4:
        nx = x -dx[direction]
        ny = y -dy[direction]
        # 뒤로 갈수 있다면 뒤로가기
        if map[nx][ny] == 0:
            x = nx
            y = ny
        else: #못가면 끝
            break
        turn_time = 0

print(count)
    

#풀이 여부: 아예 풀이 불가


