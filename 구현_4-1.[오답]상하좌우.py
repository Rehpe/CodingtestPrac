#04. 구현 - 상하좌우
#예제4-1 (page 110) 난이도 1

#N X N 좌표의 배열이 주어짐
#L, R, U, D의 키워드가 주어지고, 각각 좌, 우, 상, 하 이동을 뜻함
#여행 시작은 항상 (1,1)좌표에서 시작하며, 좌표 밖으로 나가게 되는 이동은 무시됨

#입력
# 첫째 줄에 N
# 둘째 줄에 이동할 방향들이 공백을 주고 주어짐
#출력
#최종 도착 좌표

#2차원 배열을 만들고 이동하는 방식 - 예전에 한 번 풀어본 방식이다
# 상하좌우로 움직일 때 어딜 +하고 -할 건지 헷갈리지 않기
# 실제 인덱스는 0,0부터 시작하기 때문에 이부분이 늘 헷길린다

import numpy

n = int(input())
move_plans = map(str, input().split())

coord =numpy.zeros((n+1,n+1)) #(0,0) 좌표가 헷갈리지 않게 아예 한 줄 더 큰 배열을 만든다
x, y = (1,1)

#L, R, U, D에 따른 이동 벡터값 설정
dx = {0,0,-1,1}
dy = {-1,1,0,0}
move_types = ['L','R','U','D']

for plan in move_plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
        if nx <1 or ny<1 or nx> n or ny>n:
            continue
        x, y = nx, ny

print(x,y)

#풀이 결과: 풀지 못함

#이차원 배열로 어렵게 생각할 게 아니었다
#이동하는 벡터값을 설정해준다는게 포인트인 것 같다
#만약 8방향 이동이 나오더라도 벡터값 설정을 바꿔주고, len(move_types)로 수정이 용이하다
#이런 좌표 이동 문제일 경우 dx, dy(디렉션?), nx, ny(next?) 등의 변수명을 쓰면 되겠다