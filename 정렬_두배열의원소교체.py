#정렬 - 두 배열의 원소 교체
#실전문제 4 (page182) 난이도 1

'''
N개의 원소가 들어있는 배열 A,B와 바꿔칠수 있는 횟수 K
목표는 A와 B의 원소를 총 K번 바꿔서 배열 A의 모든 값의 합이 최대가 되도록 하는 것

입력
1. N, K가 공백으로 입력
2. 둘째 줄에 a의 배열
3. 셋째 줄에 b의 배열
출력
1. A배열의 최대 합
'''

n, k = map(int, input().split())

a= list(map(int, input().split()))

b = list(map(int, input().split()))  


sorted_a = sorted(a) #a배열은 작은 순서로 정렬한다
sorted_b = sorted(b, reverse=True) #b배열은 큰 순서로 정렬한다

for i in range(k):
    if sorted_a[i] < sorted_b[i]:
        sorted_a[i] = sorted_b[i]

result = 0

for i in range(len(sorted_a)):
    result += sorted_a[i]

print(result)