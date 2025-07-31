# 1 : 익은 토마토 / 0 : 안익은 토마토 / -1 : 토마토 없음
# BFS 최단거리가 모두 익는 날짜
## bfs가 여러군데에서 동시에 일어남.. -> 한칸씩 움직일때 마다 bfs 여러 1의 좌표에서 같이하는 로직으로 구현 -> bfs에 인수를 여러개 넣는 방법
# 1과 -1을 방문처리 + tomatoMatrix에 0을 1로 바꿈
# 마지막에 visitedMatrix 순회하며 False(0)이 존재하면 -1 출력
### (D) while q에서 최대거리는 따로 관리해야함... -> 맨마지막 큐에서 꺼낸 것이 최대거리가 아닐 수 있음

'''
from collections import deque
moveList = [(1,0),(0,1),(-1,0),(0,-1)] # 대각선 x

def bfs(startNodeColRowList):
    global visitedMatrix, tomatoMatrix, m, n
    q = deque(startNodeColRowList)
    for startCol, startRow, startDist in startNodeColRowList:
        visitedMatrix[startRow][startCol] = True

    maxDist = float('-inf')
    while q:
        curCol, curRow, curDist = q.popleft()
        maxDist = max(maxDist, curDist) # (D) 최대날짜를 구해야함
        for dx, dy in moveList:
            nxtCol, nxtRow, nxtDist = curCol + dx, curRow + dy, curDist + 1
            if 0<=nxtCol<m and 0<=nxtRow<n and not visitedMatrix[nxtRow][nxtCol]:
                q.append((nxtCol, nxtRow, nxtDist))
                visitedMatrix[nxtRow][nxtCol] = True

    return maxDist # (D) 위 동일

m, n = map(int, input().split())
tomatoMatrix = [ list(map(int, input().split())) for _ in range(n) ]
visitedMatrix = [ [False]*m for _ in range(n) ]
umaiTomatoXYList = []
for row in range(n):
    for col in range(m):
        if tomatoMatrix[row][col] == 1:
            umaiTomatoXYList.append((col, row, 0))
            visitedMatrix[row][col] = True
        elif tomatoMatrix[row][col] == -1:
            visitedMatrix[row][col] = True

dayCnt = bfs(umaiTomatoXYList)
tomatoFlag = True
for colVisitedList in visitedMatrix:
    if 0 in colVisitedList:
        tomatoFlag = False
        break

if tomatoFlag:
    print(dayCnt)
else:
    print(-1)
'''
#2 bfs를 동시다발적으로 해야함 -> 최대거리를 항상 갱신하는 코드 요구

from collections import deque

moveList = [(1,0),(0,1),(-1,0),(0,-1)]

def bfs(startNodeColRowList):
    global visitedMatrix, tomatoMatrix, m, n
    q = deque(startNodeColRowList)
    # print(startNodeColRowList)
    startCol, startRow, startDist = startNodeColRowList[0][0], startNodeColRowList[0][1], startNodeColRowList[0][2]
    # print(q)
    visitedMatrix[startRow][startCol] = True

    maxDist = 0 # 아무것도 익히지 않으면 0
    while q:
        # print(f'{q=}')
        curCol, curRow, curDist = q.popleft()
        maxDist = max(maxDist, curDist)
        for dx, dy in moveList:
            nxtCol, nxtRow, nxtDist = curCol + dx, curRow + dy, curDist + 1
            if 0<=nxtCol<m and 0<=nxtRow<n and not visitedMatrix[nxtRow][nxtCol]:
                q.append((nxtCol, nxtRow, nxtDist))
                visitedMatrix[nxtRow][nxtCol] = True

    # 익은 토마토로 꽉차면
    return maxDist

m, n = map(int, input().split())
tomatoMatrix = [ list(map(int, input().split())) for _ in range(n) ]
visitedMatrix = [ [False]*m for _ in range(n) ] # 왔던곳 또 안가기 위함

# 위치가 1인 곳 찾기
startNodeColRowList = []
for row in range(n):
    for col in range(m):
        if tomatoMatrix[row][col] == 1:
            startNodeColRowList.append((col, row, 0)) # 거리도 같이 넣기
            visitedMatrix[row][col] = True # (D) 방문하면 안됨
        elif tomatoMatrix[row][col] == -1: # 벽도 True로 만들기 -> 나중에 0을 속아내려고
            visitedMatrix[row][col] = True

dayCnt = bfs(startNodeColRowList)

tomatoFlag = True
for colVisitedList in visitedMatrix:
    if 0 in colVisitedList:
        tomatoFlag = False
        break

if tomatoFlag:
    print(dayCnt)
else:
    print(-1)