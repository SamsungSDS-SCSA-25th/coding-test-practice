# 그래프 탐색 - > BFS
# 8방향 행렬로 패딩

from collections import deque

moveList = [(1,0),(-1,0),(0,1),(0,-1)]

def bfs(startCol, startRow):
    global visitedMatrix, n, m
    q = deque([(startCol, startRow)])
    visitedMatrix[startRow][startCol] = True

    while q:
        curCol, curRow = q.popleft()
        for dx, dy in moveList:
            nxtCol, nxtRow = (curCol + dx) % m, (curRow + dy) % n # (D) 논리 추가
            if 0<=nxtCol<m and 0<=nxtRow<n and not visitedMatrix[nxtRow][nxtCol]:
                q.append((nxtCol, nxtRow))
                visitedMatrix[nxtRow][nxtCol] = True

            if not (0<=nxtCol<m and 0<=nxtRow<n):
                flag = False

    return

n, m = map(int, input().split())
matrix = [ list(map(int, input().split())) for _ in range(n) ]

visitedMatrix = [[False]*m for _ in range(n)]
for row in range(n):
    for col in range(m):
        if matrix[row][col] == 1:
            visitedMatrix[row][col] = True

cnt = 0
for row in range(n):
    for col in range(m):
        if not visitedMatrix[row][col] and matrix[row][col] == 0:
            bfs(col, row)
            cnt += 1
print(cnt)