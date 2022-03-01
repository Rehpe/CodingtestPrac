#04. 구현 - 왕실의 나이트
#실전2 (page 115) 난이도 1

#나이트는
#1. 수직 두칸 이동 후 수평 한 칸
#2. 수평 두 칸 이동 후 수직 한 칸
#으로만 움직일 수 있다

# 8X8 체스칸 안에서 정원 밖으로 나가지 않고 나이트가 이동할 수 있는 경우의 수를 구하시오
#이때 행렬은 1~8 X a~h로 주어진다

#입력
#a1과 같이 좌표가 입력됨
#출력
#3 과 같이 나이트가 이동할수 있는 경우의 수 출력



#먼저 나이트가 이동할 수 있는 모든 움직임을 좌표로 구현해야한다
#현재 위치가 x,y이라고 하면
#나이트의 이동 경우의 수는 총 8가지
knight_movement = [(2,-1),(2,1),(-2,-1),(-2,1),(1,-2),(1,2),(-1,-2),(-1,2)]
count = 0

cur = str(input())
y = int(cur[1])
row = ['a','b','c','d','e','f','g','h']

for i in range(len(row)): #알파벳으로 되어있는 x값을 좌표값으로 변환
    if cur[0] == row[i]:
        x = i+1       

for i in range(len(knight_movement)):
    nx = x + knight_movement[i][0]
    ny = y + knight_movement[i][1]
    if nx < 1 or ny < 1 or nx > 8 or ny > 8:
        continue
    else:
        count +=1

print(count)


#풀이 여부: 컨닝함! (나이트가 움직일 수 있는 8방향을 구해야한다는 거 훔쳐봐서 맞힘)