#정렬 - 위에서 아래로
#실전문제 2 (page178) 난이도 1

'''
입력
1.N이 주어짐
2.N개의 수열이 입력됨
출력
1.내림차순으로 공백 구분하여 출력

'''

n = int(input())
nums = []

for _ in range(n):
    nums.append(int(input()))

nums.sort(reverse=True)

for i in range(n):
    print(nums[i], end=' ')

