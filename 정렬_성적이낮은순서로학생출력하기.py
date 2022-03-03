#정렬 - 성적이 낮은 순서로 학생 출력하기
#실전문제 3 (page180) 난이도 1

'''
입력
1.학생수 n
2. n명의 학생 이름과 점수가 공백을 두고 입력됨
출력
1.내림차순으로 학생 이름만 출력

'''

n = int(input())
score = []

for _ in range(n):
    score.append(tuple(input().split()))

def setting(list):
    return list[1]

result = sorted(score, key=setting)
result = sorted(result, reverse=True)



for names in result:
    print(names[0], end=' ')