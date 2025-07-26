# 어떤 풍선을 터뜨리면 가운데 꽃가루 개수만큼 상하좌우 풍선터짐...
# 문제를 꼼꼼히 읽자
## 동서남북을 거리 반복문에서 나누어서 분기처리

t = int(input())

# 북, 동, 남, 서
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for index in range(t):
    n, m = map(int, input().split())
    balMatrix = [ list(map(int, input().split())) for _ in range(n) ]

    maxSum = float('-inf')
    for row in range(n):
        for col in range(m):
            flowerPowder = balMatrix[row][col]
            tempSum = balMatrix[row][col] # 본인은 더하고 시작
            for dir in range(4): # 0, 1, 2, 3
                for dist in range(1, flowerPowder+1): # 꽃가루 개수만큼 반복, 본인을 반복 더하지 않게 1부터 시작
                    tempRow = row + dy[dir] * dist
                    tempCol = col + dx[dir] * dist
                    if 0 <= tempRow < n and 0 <= tempCol < m:
                        tempSum += balMatrix[tempRow][tempCol]

            maxSum = max(maxSum, tempSum)

    print(f'#{index+1} {maxSum}')