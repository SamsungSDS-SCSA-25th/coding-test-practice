t = int(input())

# 북, 동, 남, 서
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for index in range(t):
    n, m = map(int, input().split())
    balList = [ list(map(int, input().split())) for _ in range(n) ]

    maxSum = 0
    for row in range(n):
        for col in range(m):
            tempSum = balList[row][col]
            for dir in range(4):
                if 0 <= (row+dy[dir]) < n and 0 <= (col+dx[dir]) < m:
                    tempSum += balList[row+dy[dir]][col+dx[dir]]
            maxSum = max(maxSum, tempSum)

    print(f'#{index+1} {maxSum}')