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
            tempDistance = balMatrix[row][col]
            tempSum = balMatrix[row][col]
            for dir in range(4):
                for dist in range(tempDistance):
                    if dir == 0: # 북
                        if 0 <= row + dy[dir] + dist < n and 0 <= col + dx[dir] < m:
                            tempSum += balMatrix[row + dy[dir] + dist][col + dx[dir]]
                    elif dir == 1: # 동
                        if 0 <= row + dy[dir] < n and 0 <= col + dx[dir] + dist < m:
                            tempSum += balMatrix[row+dy[dir]][col+dx[dir]+dist]
                    elif dir == 2: # 남
                        if 0 <= row + dy[dir] - dist < n and 0 <= col + dx[dir] < m:
                            tempSum += balMatrix[row+dy[dir]-dist][col+dx[dir]]
                    elif dir == 3: # 서
                        if 0 <= row + dy[dir] < n and 0 <= col + dx[dir] - dist < m:
                            tempSum += balMatrix[row+dy[dir]][col+dx[dir]-dist]
            maxSum = max(maxSum, tempSum)

    print(f'#{index+1} {maxSum}')