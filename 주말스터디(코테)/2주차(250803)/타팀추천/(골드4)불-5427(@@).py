# 범위 밖으로 언제 나가는지 구하는 문제
# *좌표에서는 4방향으로 매초마다 번진다. -> 따로함수 구현
# 벽은 통과하지 못한다.

from collections import deque

# bfs 이므로 visited를 여러개 만들필요 없다 -> 재귀하지 않는다.
def burn(matrix, visited):
    burnList = []
    for row in range(n):
        for col in range(m):
            if matrix[row][col] == '*': # (D) 초기 좌표를 저장하고 불을 넣어야함...
                burnList.append((col, row))

    for col, row in burnList:
        for dx, dy in DIRECTIONS:
            nxtCol, nxtRow = col + dx, row + dy
            if 0<=nxtCol<m and 0<=nxtRow<n and not visited[nxtRow][nxtCol]:
                visited[nxtRow][nxtCol] = True
                matrix[nxtRow][nxtCol] = '*'

    return


DIRECTIONS = [(1,0), (-1,0), (0,1), (0,-1)]
def bfs(startCol, startRow, visited, matrix):
    q = deque([(startCol, startRow, 0)])
    visited[startRow][startCol] = True
    distList = []
    
    while q:
        curCol, curRow, curDist = q.popleft()
        for dx, dy in DIRECTIONS:
            nxtCol, nxtRow, nxtDist = curCol + dx, curRow + dy, curDist + 1
            if not (0<=nxtCol<m and 0<=nxtRow<n): # 탈출하는 경우
                return nxtDist

            if nxtDist not in distList:
                distList.append(nxtDist)
                burn(matrix, visited)

            if 0<=nxtCol<m and 0<=nxtRow<n and matrix[nxtRow][nxtCol] == '.' and not visited[nxtRow][nxtCol]:
                q.append((nxtCol, nxtRow, nxtDist))
                visited[nxtRow][nxtCol] = True

    return 'IMPOSSIBLE'

t = int(input())
for _ in range(t):
    m, n = map(int, input().split())
    matrix = [ list(input()) for _ in range(n) ]

    visited = [[False] * m for _ in range(n)]
    for row in range(n):
        for col in range(m):
            if matrix[row][col] == '@':
                startCol, startRow = col, row
            if matrix[row][col] == '#' or matrix[row][col] == '*':
                visited[row][col] = True
        
    print(bfs(startCol, startRow, visited, matrix))