# 3차원의 토마토

from collections import deque

moveList = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]

def bfs(startXYZList):
    global tomatoMatrix, visitedMatrix
    q = deque(startXYZList)
    # print(q)
    for startXYZ in startXYZList:
        # print(startXYZ)
        visitedMatrix[startXYZ[2]][startXYZ[1]][startXYZ[0]] = True

    maxDayCnt = 0
    while q:
        curCol, curRow, curHeight, curDist = q.popleft()
        maxDayCnt = max(maxDayCnt, curDist)
        for dx, dy, dz in moveList:
            nxtCol, nxtRow, nxtHeight, nxtDist = curCol + dx, curRow + dy, curHeight + dz, curDist + 1
            if 0<=nxtCol<m and 0<=nxtRow<n and 0<=nxtHeight<h and tomatoMatrix[nxtHeight][nxtRow][nxtCol] == 0 and not visitedMatrix[nxtHeight][nxtRow][nxtCol]:
                q.append((nxtCol, nxtRow, nxtHeight, nxtDist))
                visitedMatrix[nxtHeight][nxtRow][nxtCol] = True

    return maxDayCnt

m, n, h = map(int, input().split())
tomatoMatrix = [ [ list(map(int, input().split())) for _ in range(n) ] for _ in range(h) ]
visitedMatrix = [ [ [False]*m for _ in range(n) ] for _ in range(h) ]

startXYZList = []
for height in range(h):
    for row in range(n):
        for col in range(m):
            if tomatoMatrix[height][row][col] == 1:
                startXYZList.append((col, row, height, 0))
            elif tomatoMatrix[height][row][col] == -1:
                visitedMatrix[height][row][col] = True

dayCnt = bfs(startXYZList)

tomatoFlag = True
for height in range(h):
    for row in range(n):
        for col in range(m):
            if not visitedMatrix[height][row][col]:
                tomatoFlag = False
                break

if tomatoFlag:
    print(dayCnt)
else:
    print(-1)