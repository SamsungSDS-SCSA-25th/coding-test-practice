# 그냥 sum을 하면, 연산을 100,000 하게 된다면 시간초과 발생
# 누적합을 이용한다

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
sizes = [ tuple(map(int, input().split())) for _ in range(M) ]

preSum, preSumfix = 0, [0]
for idx in range(N):
    preSum += numbers[idx]
    preSumfix.append(preSum)

# print(preSumfix)

for start, end in sizes:
    print(preSumfix[end]-preSumfix[start-1])