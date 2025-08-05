# 범위 밖으로 언제 나가는지 구하는 문제
# *좌표에서는 4방향으로 매초마다 번진다. -> 따로함수 구현
# 벽은 통과하지 못한다.

from collections import deque
DIRECTIONS = [(1,0), (-1,0), (0,1), (0,-1)]
INF = 10**8

# bfs 이므로 visited를 여러개 만들필요 없다 -> 재귀하지 않는다.
# (D) 좌표별로 burn까지 걸리는 시간을 저장한다. -> 계속 burn을 호출하지 않기 위함
def burnBFS(startBurnList): # -> BFS로 구현해야 할듯
    global burnVisited, burnMatrix, n, m

    q = deque()
    for startCol, startRow, startSec in startBurnList:
        q.append((startCol, startRow, startSec))
        burnMatrix[startRow][startCol] = True
        burnVisited[startRow][startCol] = True

    # * 확산시키면서, *좌표 저장
    while q:
        curCol, curRow, curSec = q.popleft()
        for dx, dy in DIRECTIONS:
            nxtCol, nxtRow, nxtSec = curCol + dx, curRow + dy, curSec + 1
            if 0<=nxtCol<m and 0<=nxtRow<n and not burnVisited[nxtRow][nxtCol] and matrix[nxtRow][nxtCol] == '.':
                q.append((nxtCol, nxtRow, nxtSec))
                burnMatrix[nxtRow][nxtCol] = nxtSec
                burnVisited[nxtRow][nxtCol] = True

    return burnMatrix

def bfs(startCol, startRow):
    global matrix, burnMatrix, visited, n, m
    q = deque([(startCol, startRow, 0)])
    visited[startRow][startCol] = True
    
    while q:
        curCol, curRow, curSec = q.popleft()
        for dx, dy in DIRECTIONS:
            nxtCol, nxtRow, nxtSec = curCol + dx, curRow + dy, curSec + 1
            if not (0<=nxtCol<m and 0<=nxtRow<n): # 탈출하는 경우
                return nxtSec

            if matrix[nxtRow][nxtCol] != '.' or visited[nxtRow][nxtCol]: # 벽에 부딪히거나, 이미 방문
                continue

            if burnMatrix[nxtRow][nxtCol] <= nxtSec: # 불과 만남
                continue

            visited[nxtRow][nxtCol] = True
            q.append((nxtCol, nxtRow, nxtSec))

    return 'IMPOSSIBLE'

########################################

t = int(input())
for _ in range(t):
    m, n = map(int, input().split())
    matrix = [ list(input()) for _ in range(n) ]

    ### 초기 * 찾고, burnTime이 들어간 좌표 구하기
    burnMatrix = [[INF] * m for _ in range(n)] # burnTime 있는 좌표

    burnVisited = [[False] * m for _ in range(n)] # *용
    visited = [[False] * m for _ in range(n)] # 일반

    #1 * 위치 찾기 + . 제외하고 방문처리
    startBurnList = []
    for row in range(n):
        for col in range(m):
            if matrix[row][col] == '*':  # (D) 초기 좌표를 저장하고 불을 넣어야함...
                startBurnList.append((col, row, 0))
                burnVisited[row][col] = True
                visited[row][col] = True
            elif matrix[row][col] == '#':  # 방문 안할곳은 방문처리
                burnVisited[row][col] = True
                burnVisited[row][col] = True
                visited[row][col] = True
            elif matrix[row][col] == '@':
                startCol, startRow = col, row
                burnVisited[row][col] = True
                visited[row][col] = True

    #2 * 확산시키면서 최종 burnTime과 좌표 구하기
    burnList = burnBFS(startBurnList)

    #3 밖까지 최단거리 탐색 (제약: burnTime보다 좌표의 sec이 작아야 함)
    answer = bfs(startCol, startRow)

    print(answer)