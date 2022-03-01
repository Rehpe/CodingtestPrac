#01. 그리디 - 숫자 카드 게임
#실전 문제2 (page 96) 난이도 1

#숫자 카드가 N X M 배열로 놓여있다
# 먼저 행 하나를 고른다
# 그 행의 카드 중 제일 낮은 수의 카드를 고른다
# 이런 규칙이 있고, 가장 큰 숫자를 뽑는 결과를 출력해야함


#입력
# 첫째 줄에 공백으로 행 N, 열 M이 주어짐
# 둘째 줄부터 M만큼의 크기를 가진 배열이 N개 주어진다.
# 출력
# 뽑을 수 있는 최대 숫자 


#2차원 배열을 사용해야할것같다
# 2차원 배열을 순회하며 가장 작은 값을 우선 출력한다
#작은 숫자를 min 리스트에 넣고, min 리스트를 순회하여 가장 큰 수를 뽑는다.


N, M = map(int, input().split())
cards = []

for _ in range(N): #N만큼의 배열을 입력받는다
    cards.append(list(map(int,input().split())))

minnums = []

for i in range(0,N): #N-1만큼(0번 인덱스까지 포함이니) 리스트를 순회하며 작은 수를 찾는다
    minnums.append(min(cards[i]))

print(max(minnums))

#풀이 결과 : 정답

