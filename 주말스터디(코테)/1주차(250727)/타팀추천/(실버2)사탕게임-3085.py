
moveList = [(1,0), (0,1)] # (D) 완전탐색으로 앞방향만 확인할 것임
maxCnt = 0

n = int(input())
matrix = [ list(input()) for _ in range(n) ]

# 열 교환
for row in range(n):
    for col in range(n-1):
        # Swap
        matrix[row][col], matrix[row][col+1] = matrix[row][col+1], matrix[row][col]

        for tempRow in range(n):
            for tempCol in range(n):
                tempColor = matrix[tempRow][tempCol]
                for dx, dy in moveList:
                    tempCnt = 0 # (D) 위치...
                    for dist in range(n):
                        nxtCol, nxtRow = tempCol + dx*dist, tempRow + dy*dist
                        if 0<=nxtCol<n and 0<=nxtRow<n and matrix[nxtRow][nxtCol] == tempColor:
                            tempCnt += 1
                        else:
                            break
                    maxCnt = max(maxCnt, tempCnt)

        # 원상 복귀
        matrix[row][col], matrix[row][col + 1] = matrix[row][col + 1], matrix[row][col]

# 행 교환
for col in range(n):
    for row in range(n-1):
        # Swap
        matrix[row][col], matrix[row+1][col] = matrix[row+1][col], matrix[row][col]

        for tempRow in range(n):
            for tempCol in range(n):
                tempColor = matrix[tempRow][tempCol]
                for dx, dy in moveList:
                    tempCnt = 0 # (D) 위치...
                    for dist in range(n):
                        nxtCol, nxtRow = tempCol + dx*dist, tempRow + dy*dist
                        if 0<=nxtCol<n and 0<=nxtRow<n and matrix[nxtRow][nxtCol] == tempColor:
                            tempCnt += 1
                        else:
                            break
                    maxCnt = max(maxCnt, tempCnt)

        # 원상 복귀
        matrix[row][col], matrix[row+1][col] = matrix[row+1][col], matrix[row][col]

print(maxCnt)