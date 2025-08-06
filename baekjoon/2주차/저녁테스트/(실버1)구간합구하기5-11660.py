# M번 연산하는데, 연산할때마다 행렬을 순회하면 시간초과 발생
# M이 100,000까지 가능함 / N도 1024*1024까지 가능...
# 행렬의 누적합으로 미리계산하고 한번씩 계산하도록 순회 (*->+)
# 2차원 누적합 dp 공식 암기하기!

N, M = map(int, input().split())
matrix = [ list(map(int, input().split())) for _ in range(N) ]

dp = [ [0]*(N+1) for _ in range(N+1) ]
prefixSum = 0
for row in range(1, N+1):
    for col in range(1, N+1):
        dp[row][col] = matrix[row-1][col-1] + dp[row-1][col] + dp[row][col-1] - dp[row-1][col-1]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    print(dp[x2][y2] + dp[x1-1][y1-1] - dp[x1-1][y2] - dp[x2][y1-1])