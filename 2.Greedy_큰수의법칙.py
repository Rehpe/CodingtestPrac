#01. 그리디 - 큰 수의 법칙
#실전 문제2 (page 92) 난이도 1

#배열 N, 더하는 횟수 M, 연속 제한 K
# 배열 안 수들을 M번 더해 가장 큰 수를 만들어야 한다
# [2,4,5,3,6]에 M이 8, K가 3일 경우 6+6+6+5+6+6+6+5로 46출력
 
#공백으로 구분한 자연수 N,M,K
# 공백으로 구분된 배열 N (1이상 만 이하)
# K는 항상 M보다 작거나 같다
# 가장 큰 합을 구할 것


# 가장 큰 수와 다음으로 큰 수를 구하고 (a,b)
# M번 더하는데 K번 a를 더하고, 한 번 b를 더하고, 다시 K번 a를 더하기를 반복한다
# 즉 M - K를 하면 꼭 한 번 b를 더해야하므로 -1해야함..

N, M, K = map(int,input().split())
nums = list(map(int,input().split()))

a = max(nums) #nums의 가장 큰 값
nums.remove(a) #a를 제외한 배열을 만들고, 다시 max함수를 써 다음 큰 수 b를 구함
b = max(nums)

#더하는 규칙 = K번만큼 a를 더하고(a*K), b를 한 번 더한다(+b)
# 총 더할수 있는 횟수 M을 K+1로 나눈 몫만큼 위의 값(a*M + b)을 반복하고
# 나머지가 있다면 그만큼 a를 추가로 더해주는 식으로 문제를 푼다

result = (M // (K + 1)) * (a*K + b) 
if M % (K + 1):
    result += a *(M%(K+1))

print(result)




#풀이 결과 : 정답

