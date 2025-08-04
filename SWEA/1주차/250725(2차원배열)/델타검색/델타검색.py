t = int(input())

# 북, 동, 남, 서
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for index in range(t):
    n = int(input())
    matrix = [ list(map(int, input().split())) for _ in range(n) ]

    allSum = 0
    for row in range(n):
        for col in range(n):
            tempRow, tempCol = 0, 0
            for dir in range(4):
                tempRow = row + dx[dir]
                tempCol = col + dy[dir]
                if tempRow < 0 or tempRow >= n or tempCol < 0 or tempCol >= n:
                    continue
                allSum += abs(matrix[row][col] - matrix[tempRow][tempCol])

    print(f'#{index+1} {allSum}')