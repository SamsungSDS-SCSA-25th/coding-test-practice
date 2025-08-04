# 방향전환 1, 1, 2, 2, 3, 3 -> 2번씩 step은 +1
# 북동남서 순으로 계속 순회
# 시작은 n // 2에서 홀수임이 주어짐

n = int(input())
target = int(input())

directions = [(0,1), (1,0), (0,-1), (-1,0)]
matrix = [ [0]*n for _ in range(n) ]

num = 1
twoCnt, progressCnt, directionIdx = 2, 1, 0
while True:
    if num == n*n:
        break

    # 제일 처음은 따로
    if num == 1:
        curCol, curRow = n // 2, n // 2
        matrix[curRow][curCol] = num

        num += 1
        continue

    if twoCnt == 0:
        progressCnt += 1
        twoCnt = 2

    twoCnt -= 1
    direction = directions[directionIdx % 4]

    for dist in range(1, progressCnt+1):
        nxtCol, nxtRow = curCol + direction[0], curRow + direction[1]
        matrix[nxtRow][nxtCol] = num

        if num == n * n:
            break

        num += 1
        curCol, curRow = nxtCol, nxtRow

    directionIdx += 1

for row in range(n):
    for col in range(n):
        if matrix[::-1][row][col] == target:
            ansCol, ansRow = col, row

        print(matrix[::-1][row][col], end=' ')
    print()

print(ansRow+1, ansCol+1)