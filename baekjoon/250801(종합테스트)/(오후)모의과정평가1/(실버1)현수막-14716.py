# bfs 영역구하기

from collections import deque

moveList = [(1,0),(-1,0),(0,1),(0,-1), (1,1),(-1,-1),(1,-1),(-1,1)]
def bfs(startCol, startRow):
    global visited, matrix
    q = deque([(startCol, startRow)])
    visited[startRow][startCol] = True

    areaCnt = 0
    while q:
        # print(f'{q=}')
        curCol, curRow = q.popleft()
        for dx, dy in moveList:
            nxtCol, nxtRow = curCol + dx, curRow + dy
            if 0<=nxtCol<m and 0<=nxtRow<n and matrix[nxtRow][nxtCol] == 1 and not visited[nxtRow][nxtCol]:
                q.append((nxtCol, nxtRow))
                visited[nxtRow][nxtCol] = True
                areaCnt += 1

    # print(f'{areaCnt=}')
    return areaCnt

n, m = map(int, input().split())
matrix = [ list(map(int, input().split())) for _ in range(n) ]
# print(matrix)
visited = [ [False]*m for _ in range(n) ]
for row in range(n):
    for col in range(m):
        if matrix[row][col] == 0:
            visited[row][col] = True

cnt = 0
for row in range(n):
    for col in range(m):
        if matrix[row][col] == 1 and not visited[row][col]:
            bfs(col, row)
            cnt += 1

print(cnt)