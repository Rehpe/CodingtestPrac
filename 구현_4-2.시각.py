#04. 구현 - 시각
#예제4-2 (page 113) 난이도 1

#정수 N이 입력된다
#0시 0분 00초부터 N시 59분 59초까지의 시각 중 3이 들어간 시간을 모두 구하라

#입력
#N이 정수로 입력
#출력
#3이 들어간 모든 시각의 갯수 출력


n = int(input())
count =0

for i in range(0,n+1): #시간에 대한 for문
    for j in range(0,60): #분에 대한 for문
        for k in range(0,60): #초에 대한 for문
            if '3' in str(i) + str(j) + str(k):
                count +=1

print(count) 

#풀이 여부: 정답