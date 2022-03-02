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
        return True
    return False
        

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result += 1
    

print(result)



#37항 True가 어떻게 한 덩어리당 한번만 호출이 될 수 있는지 아직 이해가 부족함
#왜 visited[] 리스트를 따로 만들지 않고 주어진 그래프 자체를 덮어씌우는가? 괜찮은건가?
